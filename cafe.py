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
        # self.cafe = cafe
        self.name = name

    def run(self):
        # print(f"Посетитель обслуживается")
        time.sleep(5)


class Cafe:
    def __init__(self, tables):
        self.tables = tables
        self.queue = Queue(maxsize=2)
        self.costumers = []
        self.count = 0

    def customer_arrival(self, customer_qnt):
        for i in range(customer_qnt):
            obj = Customer(f'{i}')
            self.costumers.append(obj)
            time.sleep(1)
        return self.costumers

    def serve_customer(self, customer):
        for table in tables:
            if not table.is_busy:
                for cust in customer:
                    self.count += 1
                    print(f'Посетитель №{self.count} обслуживается')
                    table.is_busy += 1
                    cust.start()
                    print(f'Посетитель №{self.count} закончил')
                    cust.join()
                    table.is_busy -= 1
            else:
                print("yttttttn")
        else:
            print(f'may go to the line')



table1 = Table(1)
table2 = Table(2)
tables = [table1, table2]

cafe = Cafe(tables=tables)

atr = cafe.customer_arrival(3)
cafe.serve_customer(atr)
# customer_serve_customer = threading.Thread(target=cafe.serve_customer(atr))
# customer_serve_customer.start()
#
# # Ожидаем завершения работы прибытия посетителей
# customer_serve_customer.join()

