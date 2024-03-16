import time
from threading import Thread


spisok_numb = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
spisok_lett = ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j")


def perebor(lst, t):
    for i in lst:
        print(i)
        time.sleep(t)


thread1 = Thread(target=perebor, kwargs=dict(lst=spisok_numb, t=0.75))
thread1.start()
time.sleep(0.5)
perebor(lst=spisok_lett, t=0.75)



