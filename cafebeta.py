import threading
import time
from queue import Queue


class Table:
    def __init__(self, number):
        self.number = number
        self.is_busy = False


class Cafe:
    def __init__(self, tables):
        self.tables = [Table(number) for number in tables]
        self.queue = Queue()

    def customer_arrival(self, customer_number):
        print(f"Посетитель номер {customer_number} прибыл.", flush=True)

        for table in self.tables:
            if not table.is_busy:
                self.serve_customer(customer_number, table)
                return

        self.queue.put(customer_number)
        print(f"Посетитель номер {customer_number} ожидает свободный стол.", flush=True)

    def serve_customer(self, customer_number, current_table):
        current_table.is_busy = True
        print(f"Посетитель номер {customer_number} сел за стол {current_table.number}.", flush=True)
        time.sleep(5)
        current_table.is_busy = False
        print(f"Посетитель номер {customer_number} покушал и ушёл.", flush=True)

        if not self.queue.empty():
            next_customer = self.queue.get()
            for table in self.tables:
                if not table.is_busy:
                    self.serve_customer(next_customer, table)
                    return


class Customer(threading.Thread):
    def __init__(self, cafe, customer_number):
        super().__init__()
        self.cafe = cafe
        self.customer_number = customer_number

    def run(self):
        self.cafe.customer_arrival(self.customer_number)


tables = [1, 2, 3]
cafe = Cafe(tables)

for i in range(20):
    customer = Customer(cafe, i + 1)
    customer.start()
    time.sleep(1)
