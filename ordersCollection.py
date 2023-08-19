import uuid
from collections import defaultdict
import OrderStatus
import order
import time
import random


class Orders:
    def __init__(self):
        self.orders = defaultdict(order.Order)
        for x in range(10):
            identifier = str(uuid.uuid4())
            generated_order = order.Order(uuid=identifier, status=OrderStatus.OrderStatus.PENDING)
            self.orders[identifier] = generated_order

    def add_order(self, order_to_add: order.Order):
        self.__random_delay()
        if any(order_to_add.uuid in i for i in self.orders.keys()):
            self.orders[order_to_add.uuid].status = order_to_add.status
        else:
            self.orders[order_to_add.uuid] = order_to_add

    def remove_order(self, identifier):
        self.__random_delay()
        self.orders.pop(identifier)

    def get_all_orders(self):
        self.__random_delay()
        return list(self.orders.items())

    def get_order(self, identifier):
        self.__random_delay()
        return self.orders.get(identifier)


    @staticmethod
    def __random_delay():
        delay = random.randint(1, 3)
        time.sleep(delay)
