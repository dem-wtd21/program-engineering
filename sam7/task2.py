def add_expense():
    category = input("Введите категорию расхода: ")
    amount = input("Введите сумму: ")
    description = input("Введите описание: ")

    with open('expenses.txt', 'a', encoding='utf-8') as f:
        f.write(f"{category}|{amount}|{description}\n")
    print("Расход добавлен!")


def show_expenses():
    try:
        with open('expenses.txt', 'r', encoding='utf-8') as f:
            expenses = f.readlines()

        if not expenses:
            print("Нет записей о расходах.")
            return

        total = 0
        print("\nВСЕ РАСХОДЫ:")
        print("-" * 30)
        for line in expenses:
            category, amount, description = line.strip().split('|')
            print(f"Категория: {category}")
            print(f"Сумма: {amount} руб.")
            print(f"Описание: {description}")
            print("-" * 20)
            total += float(amount)

        print(f"ОБЩАЯ СУММА: {total} руб.")

    except FileNotFoundError:
        print("Файл с расходами не найден.")

while True:
    print("\n1 - Добавить расход")
    print("2 - Показать расходы")
    print("3 - Выход")

    choice = input("Выберите действие: ")

    if choice == '1':
        add_expense()
    elif choice == '2':
        show_expenses()
    elif choice == '3':
        print("Выход из программы")
        break
    else:
        print("Неверный выбор")