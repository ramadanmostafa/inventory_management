class WareHouse(object):
    def __init__(self, name):
        self.name = name  # the name of the warehouse
        self.inventory = {}  # dictionary that maps SKU to Quantity

    def increment(self, sku, amount=1):
        """
        This increments the inventory for the given SKU in this
        warehouse.
        :param sku: The SKU to increment from.
        :param amount: The amount to increment.
        """

        if sku not in self.inventory:
            self.inventory[sku] = 0

        self.inventory[sku] += amount

    def decrement(self, sku, amount=1):
        """
        This decrement the inventory for the given SKU in this
        warehouse.
        :param sku: The SKU to decrement from.
        :param amount: The amount to decrement.
        """
        # TODO fix race condition error
        if sku not in self.inventory:
            self.inventory[sku] = 0
            return  # can decrement below zero. This is an error.
        self.inventory[sku] -= amount

    def get_inventory_amount(self, sku):
        return self.inventory[sku]
