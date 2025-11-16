def add_two():
    try:
        number = int(input("Введите число: "))
        result = 2 + number
        print(f"Результат: {result}")
    except ValueError:
        print("Неподходящий тип данных. Ожидалось число.")

if __name__ == '__main__':
    add_two()
    add_two()
    add_two()