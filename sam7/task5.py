def add_wish():
    wish = input("Введите ваше пожелание на день: ")
    with open('wishes.txt', 'a', encoding='utf-8') as f:
        f.write(wish + '\n')
    print("Пожелание добавлено!")


def show_wishes():
    try:
        with open('wishes.txt', 'r', encoding='utf-8') as f:
            wishes = f.readlines()

        if not wishes:
            print("Пожеланий пока нет.")
            return

        print("\nвсе пожелания:")
        print("-" * 20)
        for i, wish in enumerate(wishes, 1):
            print(f"{i}. {wish.strip()}")

    except FileNotFoundError:
        print("Файл с пожеланиями не найден.")


while True:
    print("\n1 - Добавить пожелание")
    print("2 - Показать пожелания")
    print("3 - Выход")

    choice = input("Выберите действие: ")

    if choice == '1':
        add_wish()
    elif choice == '2':
        show_wishes()
    elif choice == '3':
        print("Хорошего дня!")
        break
    else:
        print("Неверный выбор")