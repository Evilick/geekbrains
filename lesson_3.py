# Первое задание
def my_func(first_number, second_number):
    try:
        return first_number // second_number
    except ZeroDivisionError:
        return 'Делить на ноль нельзя!'
    except ValueError:
        return 'Вы ввели не число!'


user_numbers = my_func(int(input('Введите первое число: ')), int(input('Введите второе число: ')))
print('Результат деления первого числа на второе:', user_numbers)


# Второе задание
def my_func(name, surname, year, city, email, phone):
    print(name, surname, year, city, email, phone)


my_func(name='Ринат', surname='Ханов', year='1994', city='Санкт-Петербург', email='abc@mail.ru', phone='7777')


# Третье задание
def my_func(first_number, second_number, third_number):
    if first_number >= third_number and second_number >= third_number:
        return first_number + second_number
    elif second_number < first_number < third_number:
        return first_number + third_number
    else:
        return second_number + third_number


my_sum = my_func(5, 6, 2)
print('Сумма двух наибольших чисел:', my_sum)


# Четвертое задание
def my_func(x, y):
    return 1 / x ** abs(y)


print(my_func(2, -3))


# Шестое задание
def my_func(a):
    return a.title()


print(my_func(input('Введите слово: ')))
