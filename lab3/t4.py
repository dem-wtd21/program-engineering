numbers = [2, 5, 6, 8, 9, 11, 15, 17, 54, 224]
value = int(input('Введите значение переменной: '))
if value in numbers:
    if value % 2 == 0:
        print('Переменная четная и есть в массиве numbers')
    else:
        print('Переменная нечетная и есть в массиве numbers')
else:
    print(f'Переменной нет в массиве numbers и она равна {value}')