from typing import Optional
import OrderStatus
from pydantic import BaseModel


class Order(BaseModel):
    uuid: str
    status: OrderStatus = OrderStatus.OrderStatus.PENDING

    def execute(self):
        print(f"Executing order, {self.uuid}")
        self.status = OrderStatus.OrderStatus.EXECUTED
        print(f"Executed order, {self.uuid}")

    def cancel(self):
        print(f"Cancelling order, {self.uuid}")
        self.status = OrderStatus.OrderStatus.CANCELLED
        print(f"Canceled order, {self.uuid}")

    def set_pending(self):
        print(f"Setting to pending, order, {self.uuid}")
        self.status = OrderStatus.OrderStatus.PENDING
        print(f"Setting to pending,, {self.uuid}")
