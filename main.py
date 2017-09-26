from order import Order
from warehouse import WareHouse
from seller import Seller
import threading


threadLock = None


class myThread(threading.Thread):
    """
    class to handle multiple threads
    """
    def __init__(self, threadID, name, counter, seller):

        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
        self.seller = seller

    def run(self):
        # Get lock to synchronize threads
        threadLock.acquire()
        if self.threadID == 1:
            order = Order(order_sku="APP", order_amount=2400)
            self.seller.process_order(order, delay=5)
            print("thread1")
            print_order_info(order)

        elif self.threadID == 2:
            order = Order(order_sku="APP", order_amount=2400)
            self.seller.process_order(order, 1)
            print("thread2")
            print_order_info(order)

        elif self.threadID == 3:
            order = Order(order_sku="APP", order_amount=2400)
            self.seller.process_order(order, 2)
            print("thread3")
            print_order_info(order)

        elif self.threadID == 4:
            order = Order(order_sku="APP", order_amount=2400)
            self.seller.process_order(order, 3)
            print("thread4")
            print_order_info(order)

        elif self.threadID == 5:
            order = Order(order_sku="APP", order_amount=2400)
            self.seller.process_order(order, 2)
            print("thread5")
            print_order_info(order)

        elif self.threadID == 6:
            order = Order(order_sku="APP", order_amount=2400)
            self.seller.process_order(order, 7)
            print("thread6")
            print_order_info(order)

        elif self.threadID == 7:
            order = Order(order_sku="APP", order_amount=2400)
            self.seller.process_order(order, 12)
            print("thread7")
            print_order_info(order)

        elif self.threadID == 8:
            order = Order(order_sku="APP", order_amount=2400)
            self.seller.process_order(order, 1)
            print("thread8")
            print_order_info(order)

        elif self.threadID == 9:
            order = Order(order_sku="APP", order_amount=2400)
            self.seller.process_order(order, 5)
            print("thread9")
            print_order_info(order)

        elif self.threadID == 10:
            order = Order(order_sku="APP", order_amount=2400)
            self.seller.process_order(order, 0)
            print("thread10")
            print_order_info(order)

        # Free lock to release next thread
        threadLock.release()


def print_seller_info(seller):
    # print seller info
    print("----------------------------")
    print("-------------seller---------------")
    print("seller name", seller.name)
    for warehouse_name, warehouse in seller.warehouses.items():
        print("----------------------------")
        print("warehouse name:", warehouse.name)
        print("warehouse inventory", warehouse.inventory)

    print("----------------------------")
    print("----------------------------")


def print_order_info(order):
    print("----------------------------")
    print("----------order--------------")
    print("acknowledged", order.acknowledged)
    print("canceled", order.canceled)
    print("shipped", order.shipped)
    print("rejected", order.rejected)
    print("tracking_number", order.tracking_number)
    print("order_sku", order.order_sku)
    print("order_amount", order.order_amount)
    print("----------------------------")
    print("----------------------------")


def main():
    california_warehouse = WareHouse("California")
    california_warehouse.increment("APP", 500)
    california_warehouse.increment("ORG", 200)

    newyork_warehouse = WareHouse("NewYork")
    newyork_warehouse.increment("APP", 1200)
    newyork_warehouse.increment("ORG", 700)

    cairo_warehouse = WareHouse("Cairo")
    cairo_warehouse.increment("APP", 1500)
    cairo_warehouse.increment("ORG", 1000)

    john_seller = Seller("John")
    john_seller.add_warehouse(california_warehouse)
    john_seller.add_warehouse(newyork_warehouse)
    john_seller.add_warehouse(cairo_warehouse)

    global threadLock
    threadLock = threading.Lock()

    threads = []

    # Create new threads
    thread1 = myThread(1, "Thread-1", 1, seller=john_seller)
    thread2 = myThread(2, "Thread-2", 2, seller=john_seller)
    thread3 = myThread(3, "Thread-3", 3, seller=john_seller)
    thread4 = myThread(4, "Thread-4", 4, seller=john_seller)
    thread5 = myThread(5, "Thread-5", 5, seller=john_seller)
    thread6 = myThread(6, "Thread-6", 6, seller=john_seller)
    thread7 = myThread(7, "Thread-7", 7, seller=john_seller)
    thread8 = myThread(8, "Thread-8", 8, seller=john_seller)
    thread9 = myThread(9, "Thread-9", 9, seller=john_seller)
    thread10 = myThread(10, "Thread-10", 10, seller=john_seller)

    # Start new Threads
    thread1.start()
    thread2.start()
    thread3.start()
    thread4.start()
    thread5.start()
    thread6.start()
    thread7.start()
    thread8.start()
    thread9.start()
    thread10.start()

    # Add threads to thread list
    threads.append(thread1)
    threads.append(thread2)
    threads.append(thread3)
    threads.append(thread4)
    threads.append(thread5)
    threads.append(thread6)
    threads.append(thread7)
    threads.append(thread8)
    threads.append(thread9)
    threads.append(thread10)

    # Wait for all threads to complete
    for t in threads:
        t.join()
    print("Exiting Main Thread")

    print_seller_info(john_seller)


if __name__ == '__main__':
    main()
