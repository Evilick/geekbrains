# Задание №1
list = []
while True:
    line = input("Введите слово: ")
    if line == '':
        print(list)
        break
    else:
        next_line = line + '\n'
        list.append(next_line)

    with open("task_1.txt", "w") as file_obj:
        file_obj.writelines(list)
        print(file_obj)

# Задание №2
with open('task_2.txt', 'r') as f_obj:
    content = f_obj.readlines()
    print(f'Количество строк в файле - {len(content)}')
    for i in range(len(content)):
        print(f'Количество символов в {i + 1} - ой строке: {len(content[i])}')
with open('task_2.txt', 'r') as f_obj:
    content = f_obj.read()
    content = content.split()
    print(f'Общее количество слов - {len(content)}')

# Задание №3
summ = 0
count = 0
persons = []
with open("salary.txt") as file_obj:
    for line in file_obj:
        tokens = line.split(':')
        if int(tokens[1]) <= 20000:
            persons.append(tokens[0])
        summ += int(tokens[1])
        count += 1
result = summ / count
print(f"Персонал с доходом < 20000: {persons}")
print(f"Средний доход: {result}")


# Задание № 5
def summ():
    try:
        with open('zadanie.txt', 'w+') as file_obj:
            line = input('Введите цифры через пробел: \n')
            file_obj.writelines(line)
            numb = line.split()
            print(sum(map(int, numb)))
    except IOError:
        print('Ошибка в файле')
    except ValueError:
        print('Неправильно набран номер. Ошибка ввода-вывода')
summ()

# Задание 4
rus = {'One' : 'Один', 'Two' : 'Два', 'Three' : 'Три', 'Four' : 'Четыре'}
new_file = []
with open('translate.txt', 'r') as file_obj:
    for i in file_obj:
        i = i.split(' ', 1)
        new_file.append(rus[i[0]] + '  ' + i[1])
    print(new_file)

