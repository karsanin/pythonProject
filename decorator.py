def is_prime(func):
    def wrapper(*args):
        print(func(*args))
        n = func(*args)
        if n % 2 == 0:
            return print("Составное")
        d = 3
        while d * d <= n and n % d != 0:
            d += 2
        if d * d > n:
            print("Простое")
        else:
            print("Составное")
    return wrapper


@is_prime
def summa(a, b, c):
    result = a + b + c
    return result


summa(0, 3, 20)
