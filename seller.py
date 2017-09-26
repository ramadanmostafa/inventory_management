import time
from order_manager import OrderManager


class Seller(object):
    def __init__(self, name):
        self.name = name  # the name of the seller
        self.warehouses = {}

    def add_warehouse(self, warehouse):
        self.warehouses[warehouse.name] = warehouse

    def remove_warehouse(self, warehouse_name):

        flag = False
        if warehouse_name in self.warehouses:
            del self.warehouses[warehouse_name]
            flag = True

        return flag

    def process_order(self, order, delay=0):
        order_manager = OrderManager(self)
        is_acknowledged = order_manager.acknowledge_order(order)
        time.sleep(delay)
        if is_acknowledged:
            print("order is acknowledged")
            print(order.acknowledged)
            print(order.rejected)
            print(order_manager.warehouses)
            order_manager.ship_order(order=order)
        else:
            print("There is no inventory for this order")
            print(order.acknowledged)
            print(order.rejected)
            print(order_manager.warehouses)
