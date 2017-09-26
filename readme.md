Problem 2 - Inventory Management
This is a simplified real world problem of inventory management. 
If not done carefully, race conditions might occurs and therefore the system might report the wrong inventory amount. You are trying to build an error-proof inventory management system.

An Inventory Management Systems would have

Seller: this is the person/company that is selling different products.

SKUs: these are the identifiers of the product a seller sells.

WareHouses: these are the locations where the products are stored.

Inventory Quantity: this is the amount of units the seller has for each SKU in each warehouse.

Order: this is created when a customer buys a product. The inventory management system should decrease inventory when an order is received and processed. There are two steps in processing an order.

Step 1: the seller acknowedges the customer that the order will be fulfilled. The seller may also reject the order and let the customer know that it cannot be fulfilled.

Step 2: the seller ships the order and provides a tracking number. The seller may also cancel the order even after acknowledging. It happens. Hopefully not the fault of our inventory management system.

Here is a scenario to help you understand the above concepts.

Seller Name: John. He sells fruits.

SKUs: John sells two type of fruits. Apples and Oranges.

SKU for Apple: APP

SKU for Orange: ORG

Warehouses: John has two warehouses. One in California and another in NewYork. The name of those warehouses are "California Warehouse" and "NewYork Warehouse"

Inventory Quantity: John has the following quantity in each warehouse.

California Warehouse: APP is 500 and ORG is 200

NewYork Warehouse: APP is 1200 and ORG is 700

Order: John just received an order for 10 oranges. He is going to ship 5 from California Warehouse and 5 from the NewYork Warehouse. When all is done, California warehouse will have 195 oranges and New York Warehouse will have 695 oranges.

Your tasks is to complete the code below. The code below is going to be run concurrently whenever a seller receives an order. A seller could receive two or more orders at the same time. Note: code is not tested. Fix any syntax or logical errors you find.

Determine where there could be a race condition and make them atomic using python3. Complete the logic of the OrderManager class so that:

We never acknowledge an order that we do not have inventory for.

We never reject an order that we have inventory for.

Write an end to end test for this code. The test should create a possible race condition scenario and assert that the system handles it properly.


    class WareHouse(object):
        def __init__(self, name):
            self.name = name   # the name of the warehouse
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
    
            self.inventory[sku] += 1
     
        def decrement(self, sku, amount=1):
            """
            This decrement the inventory for the given SKU in this 
            warehouse.
            :param sku: The SKU to decrement from.
            :param amount: The amount to decrement.
            """
            if sku not in self.inventory: 
                self.inventory[sku] = 0
                return  # can decrement below zero. This is an error.
            self.inventory[sku] -= 1


    class Order(object):
    
       def __init__(self):
            self.acknowledged = False  
            self.canceled = False
            self.shipped = False
            self.rejected = False
            self.tracking_number = ""
    
    
    class OrderManager(object):
    
        def __init__(self):  
            # dictionary that maps warehouse name to warehouse object
            self.warehouses = {} 
    
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
            if True:
                order.acknowledged = True
                return True
            else:
                order.rejected = True
                return False
    
        def ship_order(self, order, tracking_number, warehouse_name):
            """
            At this point, the order has been shipped and seller has 
            determined which warehouse they will be shipping from.
            :param order: the order to ship
            :param tracking_number: Tracking Number of the shipment
            :param warehouse_name: Name of WareHouse it was Shipped From.
            :return: True if Shipped False otherwise.
    
            Perform any inventory management you need to do here.
            """
            order.shipped = True
            order.tracking_number = tracking_number
            return order.shipped
        
        def cancel_order(self, order):
            """
            Sometimes, seller cancels after he/she has acknowledged 
            the order.
            :param order: Order to Cancel
            :return: True if canceled False otherwise.
    
            Perform any inventory management you need to do here.
            """
            order.canceled = True
            return order.canceled
	
	
Notes

to run it just run the main.py file, it will generate 10 threads and will try to buy about 2400 orange from the seller each time.
i used synchronizing threads to make sure race condition won't happen but my code will work also if used normal threads.
to test it just comment line 24 and line 86 in main.py then first order will be shipped only and the other orders will be 
acknowledged then will be cancelled.
