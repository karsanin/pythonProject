print(f'{'  Задача №1"  ':*^65}')


def create_operation(operation):
    if operation == "multiply":
        def multiply(x, y):
            return x * y
        return multiply
    elif operation == "divide":
        def divide(x, y):
            try:
                return x / y
            except ZeroDivisionError:
                return "Ошибка: Деление на ноль."
        return divide


my_func_add1 = create_operation("divide")
my_func_add2 = create_operation("multiply")
print(my_func_add1(10, 0))
print(my_func_add2(10, 2))

print(f'{'  Задача №2"  ':*^65}')


def mult_def(x):
    return x ** 2


square_number = lambda x: x ** 2
print(square_number(11))
print(mult_def(12))

print(f'{'  Задача №3"  ':*^65}')


class Rect:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __call__(self):
        return self.a * self.b


area = Rect(6, 6)
print(f'Сторона а - {area.a}\nСторона b - {area.b}\nПлощадь - {area()}')
