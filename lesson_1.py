# Задание №1
a = 150
b = 130
print('Вы ввели переменные a и b: ', a, b)
first_line = input('Введите первую строку: ')
first_number = int(input('Введите первое число: '))
second_line = input('Введите вторую строку: ')
second_number = int(input('Введите второе число: '))

print(f'Первая строка и цифра: {first_line}, {first_number}\nВторая строка и цифра: {second_line}, {second_number}')

# Задание №2
user_time = int(input('Введите время в секундах: '))
hour = user_time // 3600
minute = (user_time - hour * 3600) // 60
second = user_time - (hour * 3600 + minute * 60)
print(f'Время: {hour}:{minute}:{second}')

# Задание №3
n = int(input('Введите число: '))
amount = n + int(str(n) + str(n)) + int(str(n) + str(n) + str(n))
print(f'Сумма в формате n + nn + nnn: {amount}')

# Задание №5
income = int(input('Введите выручку фирмы в рублях: '))
costs = int(input('Введите издержки фирмы в рублях: '))
profitability = income // costs
if income > costs:
    print(f'Фирма работает прибыльно. Рентабельность составила: {profitability}')
    staff = int(input('Введите число сотрудников фирмы: '))
    staff_profitability = income // staff
    print(f'Прибыль в расчете на одного сотрудника составила: {staff_profitability}')
else:
    print('Фирма работает в убыток')

# Задание №6
a = int(input('Сколько километров вы пробежали за первый день: '))
b = int(input('Введите желаемое число километров: '))
days = 1
while a < b:
    a = a + a * 0.1
    days += 1

print(f'Вы достигнете желаемого результата за {days} дней')
