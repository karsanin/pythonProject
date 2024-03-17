import threading
import time

lock_a = threading.RLock()
lock_b = threading.RLock()


class BankAccount:

    def __init__(self, name, balance):
        self.balance = balance
        self.name = name

    def deposit(self, amount):
        with lock_a:
            self.balance += amount
            print(f'Баланс пополнен на {amount}, Итого на счету {self.balance}')

    def withdraw(self, amount):
        with lock_b:
            self.balance -= amount
            print(f'С баланса списано {amount}, Итого на счету {self.balance}')


account = BankAccount(name="First", balance=1000)


def deposit_task(acc, amount):
    for _ in range(100):
        acc.deposit(amount)
        time.sleep(0)


def withdraw_task(acc, amount):
    for _ in range(100):
        acc.withdraw(amount)
        time.sleep(0)


deposit_thread = threading.Thread(target=deposit_task, args=(account, 10))
withdraw_thread = threading.Thread(target=withdraw_task, args=(account, 15))

deposit_thread.start()
withdraw_thread.start()

deposit_thread.join()
withdraw_thread.join()
