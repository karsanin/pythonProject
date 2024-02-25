import warnings


def divide(a, b):
    try:
        print(f'Будем делить {a} на {b}')
        if b <= 0.01:
            warnings.warn("Внимание, делитель приближается к нулю!!!", UserWarning)
        else:
            return a / b
    except UserWarning as exc:
        print(f"Предупреждение как исключение {exc}")
    finally:
        print(a / b)

print('фильтр первый - ERROR')
warnings.simplefilter('error', UserWarning)
divide(1000, 0.001)

# print('фильтр второй - IGNORE')
# warnings.simplefilter('ignore', UserWarning)
# divide(1000, 0.001)

# print('фильтр третий - ALWAYS')
# warnings.simplefilter('always', UserWarning)
# divide(1000, 0.001)
