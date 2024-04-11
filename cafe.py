import threading
import time
from queue import Queue


class Table:
    def __init__(self, number):
        self.number = number
        self.is_busy = False


class Customer(threading.Thread):
    def __init__(self, name):
        super().__init__()
        self.cafe = cafe
        self.name = name

    def run(self):
        print(f"Посетитель {self.name} прибыл")
        self.cafe.serve_customer(self)


class Cafe:
    def __init__(self, tables):
        self.tables = tables
        self.queue = Queue()
        # self.costumers = []
        self.count = 0

    def customer_arrival(self):
        for i in range(5):
            obj = Customer(f'{i+1}')
            obj.start()
            time.sleep(1)



    def serve_customer(self, customer):
        self.queue.put(customer.name)
        while not self.queue.empty():
            for table in tables:
                if not table.is_busy:
                    table.is_busy += 1
                    name = self.queue.get()
                    print(f'Посетитель #{name} сел за стол № {table.number}, обслуживается')
                    time.sleep(5)
                    print(f'Посетитель #{name} закончил, стол № {table.number} свободен')
                    table.is_busy -= 1


table1 = Table(1)
table2 = Table(2)
table3 = Table(3)
tables = [table1, table2, table3]

cafe = Cafe(tables=tables)


customer_arrival_thread = threading.Thread(target=cafe.customer_arrival)
customer_arrival_thread.start()

# Ожидаем завершения работы прибытия посетителей
customer_arrival_thread.join()
