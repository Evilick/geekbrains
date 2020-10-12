# Задание №1 отдельным файлом
# Задание №2
main_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
new_list = [el for num, el in enumerate(main_list) if main_list[num - 1] <= main_list[num]]
print(new_list)

# Задание №3
print(f'{[el for el in range(20, 241) if el % 20 == 0 or el % 21 == 0]}')

# Задание №4
my_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
new_list = [el for el in my_list if my_list.count(el) < 2]
print(new_list)

# Задание №5
from functools import reduce


def my_func(first_el, second_el):
    return first_el * second_el


print(f'Перемножение всех элементов списка: {reduce(my_func, [el for el in range(100, 1001) if el % 2 == 0])}')

# Задание № 7
from itertools import count
from math import factorial


def fibo_gen():
    for el in count(1):
        yield factorial(el)


numbers = fibo_gen()
x = 0
for i in numbers:
    if x <= 15:
        print(i)
        x += 1
    else:
        break
