from fastapi import WebSocket


class Broadcaster:
    def __init__(self):
        self.subscribers = []

    async def subscribe(self, websocket: WebSocket):
        await websocket.accept()
        self.subscribers.append(websocket)

    async def unsubscribe(self, websocket: WebSocket):
        self.subscribers.remove(websocket)

    async def broadcast(self, data: str):
        for subscriber in self.subscribers:
            await subscriber.send_text(f"broadcasting {data}")
