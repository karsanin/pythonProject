class MyExc1(Exception):

    def __init__(self, mess):
        self.mess = mess

    pass


class MyExc2(Exception):

    def __init__(self, mess):
        self.mess = mess

    pass


def divide(x, y):
    if isinstance(x, str):
        raise MyExc2("Делить можно только числа!!!")
    elif y == 0:
        raise MyExc1('Ну кто же делит на ноль!!!')
    return x / y


mylist = [10, 100, 1000, "10000", 100000]
for x in mylist:
    for y in range(2):

        try:
            divide(x, y)
        except MyExc1 as exc1:
            print(f'Ошибка - {exc1}')
        except MyExc2 as exc2:
            print(f'Ошибка - {exc2}')
        else:
            result = x / y
            print(result)
        finally:
            print("*"*20)
