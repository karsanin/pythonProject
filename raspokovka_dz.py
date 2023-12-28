def print_params(a=1, b='строка', c=True):
    print(a)
    print(b, c)


print_params(a=50)
print_params(a=50, b='столбец')
print_params(a=2, b='red', c=False)
print_params()
# print_params(b = 25)
# print_params(c = [1,2,3])

values_list = [5, 'six', {'seven': 7}]
values_dict = {'a': 'one', 'b': 555, 'c': 1000}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = ['sting', 707]
print_params(*values_list_2, 42)
