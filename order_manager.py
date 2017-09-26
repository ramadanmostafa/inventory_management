class OrderManager(object):
    def __init__(self, seller):
        # dictionary that maps warehouse name (to be shipped from) to amount.
        self.warehouses = {}
        self.seller = seller

        # dictionary that keeps track of amounts decremented from warehouses so that it'll be easy to cancel an order,
        # in case of race condition.
        self.shipped_amounts = {}

    def acknowledge_order(self, order):
        """
        :param order: the order to acknowledge
        :return: True if Acknowledged False otherwise.

        At this point, the seller has acknowledged that they will
        ship the order. However, the we do not know which warehouse
        it will be shipped from.

        We only acknowledge if we have enough inventory. Fix the
        code below to only acknowledge when inventory is available
        in any warehouse. Perform any inventory management you need
        to do.
        """
        total_amount = 0
        acknowledged_amount = 0
        for warehouse_name, warehouse in self.seller.warehouses.items():
            if order.order_sku in warehouse.inventory:
                total_amount += warehouse.inventory[order.order_sku]
                if total_amount >= order.order_amount:
                    order.acknowledged = True
                    self.warehouses[warehouse_name] = order.order_amount - acknowledged_amount
                    return True
                else:
                    self.warehouses[warehouse_name] = warehouse.inventory[order.order_sku]
                    acknowledged_amount += self.warehouses[warehouse_name]

        order.rejected = True
        self.warehouses = {}
        return False

    def ship_order(self, order):
        """
        At this point, the order has been shipped and seller has
		determined which warehouse they will be shipping from.
		:param order: the order to ship
		:param tracking_number: Tracking Number of the shipment
        :return: True if Shipped False otherwise.

        Perform any inventory management you need to do here.
        """
        for warehouse_name, amount in self.warehouses.items():
            self.seller.warehouses[warehouse_name].decrement(
                sku=order.order_sku,
                amount=self.warehouses[warehouse_name]
            )
            self.shipped_amounts[warehouse_name] = self.warehouses[warehouse_name]
            if self.seller.warehouses[warehouse_name].get_inventory_amount(sku=order.order_sku) < 0:
                self.cancel_order(order)
                return False
        order.shipped = True
        return order.shipped

    def cancel_order(self, order):
        """
        Sometimes, seller cancels after he/she has acknowledged
        the order.
        :param order: Order to Cancel
        :return: True if canceled False otherwise.

        Perform any inventory management you need to do here.
        """
        for warehouse_name, amount in self.shipped_amounts.items():
            self.seller.warehouses[warehouse_name].increment(
                sku=order.order_sku,
                amount=amount
            )
        order.canceled = True
        return True
