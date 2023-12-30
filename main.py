def test_zap(a, b, c=100, *args, **kwargs):
    print(test_zap)
    for i in list(args):
        print('переменные списка:', i)
    for key in dict(kwargs):
        print('dictionary', key)


test_zap(3, 6, 55, 77, 55, key='fff', door='дверь')


def fact(n):
    if n == 1:
        return 1
    less_fact = fact(n=n - 1)
    return n * less_fact


print(fact(11))
