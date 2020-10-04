# Задание №1
my_list = [1, 'Hello, python world!', 2.8, (1, 2, 3), [4, 5, 6], True, None, {'country': 'Russia', 'capital': 'Moscow'}]
for list_item in my_list:
    print(f'{list_item} is a {type(list_item)}')

# Задание №2
my_list = [1, 2, 3, 4, 5]
if len(my_list) % 2 == 0:
    i = 0
    while i < len(my_list):
        element = my_list[i]
        my_list[i] = my_list[i+1]
        my_list[i+1] = element
        i += 2
else:
    i = 0
    while i < len(my_list) - 1:
        element = my_list[i]
        my_list[i] = my_list[i + 1]
        my_list[i + 1] = element
        i += 2
print(my_list)

# Задание №3
# Метод с list
seasons_list = ['зима', 'весна', 'лето', 'осень']
month = int(input("Введите номер месяца от 1 до 12: "))
if month == 1 or month == 2 or month == 12:
    print(f'Это {seasons_list[0]}')
elif month == 3 or month == 4 or month == 5:
    print(f'Это {seasons_list[1]}')
elif month == 6 or month == 7 or month == 8:
    print(f'Это {seasons_list[2]}')
elif month == 9 or month == 10 or month == 11:
    print(f'Это {seasons_list[3]}')
else:
    print("Вы ввели не корректный номер месяца")

# Метод с dict
seasons_dict = {1: 'зима', 2: 'весна', 3: 'лето', 4: 'осень'}
month = int(input("Введите номер месяца от 1 до 12: "))
if month == 1 or month == 12 or month == 2:
    print(f'Это {seasons_dict.get(1)}')
elif month == 3 or month == 4 or month == 5:
    print(f'Это {seasons_dict.get(2)}')
elif month == 6 or month == 7 or month == 8:
    print(f'Это {seasons_dict.get(3)}')
elif month == 9 or month == 10 or month == 11:
    print(f'Это {seasons_dict.get(4)}')
else:
    print("Вы ввели не корректный номер месяца")

# Задание №4
my_stroke = input("Введите строку: ")
a = my_stroke.split(' ')
for i, element in enumerate(a, 1):
    if len(element) > 10:
        element = element[0:10]
    print(f"{i}. {element}")

# Задание №5
number = int(input("Введите номер: "))
my_list = [7, 5, 3, 3, 2]
a = my_list.count(number)
for element in my_list:
    if a > 0:
        i = my_list.index(number)
        my_list.insert(i+a, number)
        break
    else:
        if number > element:
            b = my_list.index(element)
            my_list.insert(b, number)
            break
        elif number < my_list[len(my_list) - 1]:
            my_list.append(number)
print(my_list)
