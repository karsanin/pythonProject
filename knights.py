from threading import Thread
import time

class Knight(Thread):

    def __init__(self, name, skill, *args):
        super().__init__(*args)
        self.name = name
        self.skill = skill
        self.days_defend = 0

    def run(self):
        enemy = 100
        print(f'{self.name}, на нас напали!')
        while enemy > 0:
            time.sleep(1)
            enemy -= self.skill
            self.days_defend += 1
            print(f'Шёл {self.days_defend} день атаки, {self.name} поверг {self.skill} врагов, но их было ещё {enemy}!')
        else:
            print(f'Враги повержены, спасибо {self.name}, осада закончилась за {self.days_defend}')


knight1 = Knight("Sir Lancelot", 10)  # Низкий уровень умения
knight2 = Knight("Sir Galahad", 20)  # Высокий уровень умения

knight1.start()
knight2.start()

knight1.join()
knight2.join()
