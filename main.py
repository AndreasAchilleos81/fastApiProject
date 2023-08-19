from fastapi import FastAPI, WebSocket, HTTPException
from fastapi.responses import HTMLResponse

from OrderStatus import OrderStatus
from order import Order
from ordersCollection import Orders
from broadcaster import Broadcaster

broadcaster: Broadcaster = Broadcaster()
app = FastAPI()
orders_collection: Orders = Orders()

html = """
<!DOCTYPE html>
<html>
    <head>
        <title>Chat</title>
    </head>
    <body>
        <h1>WebSocket Chat</h1>
        <form action="" onsubmit="sendMessage(event)">
            <input type="text" id="messageText" autocomplete="off"/>
            <button>Send</button>
        </form>
        <ul id='messages'>
        </ul>
        <script>
            var ws = new WebSocket("ws://localhost:8000/ws");
            ws.onmessage = function(event) {
                var messages = document.getElementById('messages')
                var message = document.createElement('li')
                var content = document.createTextNode(event.data)
                message.appendChild(content)
                messages.appendChild(message)
            };
            function sendMessage(event) {
                var input = document.getElementById("messageText")
                ws.send(input.value)
                input.value = ''
                event.preventDefault()
            }
        </script>
    </body>
</html>
"""


@app.get("/")
async def get():
    return HTMLResponse(html)


@app.get("/orders", status_code=200)
async def get():
    orders = orders_collection.get_all_orders()
    await broadcaster.broadcast("All orders returned")
    return orders


@app.get("/orders/{order_id}", status_code=200)
async def get(order_id: str):
    order = orders_collection.get_order(order_id)
    if order is None:
        await broadcaster.broadcast(f"Order with id: {order_id} was not found")
        raise HTTPException(status_code=404, detail="Order not found")
    await broadcaster.broadcast(f"Found and returning {order.uuid} status:{order.status}")
    return order


@app.delete("/orders/{order_id}", status_code=204)
async def delete_order(order_id: str):
    order = orders_collection.get_order(order_id)
    if order is None:
        raise HTTPException(status_code=404, detail="Order not found")
    order.status = OrderStatus.CANCELLED
    orders_collection.add_order(order)
    await broadcaster.broadcast(f"Found and deleted {order.uuid} status:{order.status}")


@app.post("/orders", response_model=Order, status_code=201)
async def post(order: Order) -> Order:
    try:
        orders_collection.add_order(order)
    except Exception as e:
        await broadcaster.broadcast(f"Order: {order.uuid} status: {order.status} has not being added due to error")
        raise HTTPException(status_code=400, detail=f"Invalid input, stacktrace: {e}")

    await broadcaster.broadcast(f"Order with id: {order.uuid} and status {order.status} has been added/updated")
    return order


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await broadcaster.subscribe(websocket)
    while True:
        data = await websocket.receive_text()
        await broadcaster.broadcast(data)
