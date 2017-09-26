import random


class Order(object):

    def __init__(self, order_sku, order_amount):
        self.acknowledged = False
        self.canceled = False
        self.shipped = False
        self.rejected = False
        self.tracking_number = str(int(random.random() * 1000000000000000))
        self.order_sku = order_sku
        self.order_amount = order_amount
