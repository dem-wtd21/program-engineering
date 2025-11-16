class StyleDecorator:
    # Конструктор класса-декоратора, принимает функцию для декорирования
    def __init__(self, func):
        self.func = func  # Сохранение исходной функции

    # Метод __call__ вызывается при вызове декорированной функции
    def __call__(self, *args, **kwargs):
        print("Начало оформления функции")  # Сообщение перед выполнением
        print("-" * 40)  # Декоративная линия
        result = self.func(*args, **kwargs)  # Вызов исходной функции
        print("-" * 40)  # Декоративная линия
        print("Оформление завершено")  # Сообщение после выполнения
        return result  # Возвращаем результат исходной функции


# Применяем декоратор к первой функции
@StyleDecorator
def greet(name):
    # Функция приветствия пользователя
    print(f"Привет, {name}!")
    return f"Пользователь {name} приветствован"


# Применяем декоратор ко второй функции
@StyleDecorator
def calculate_sum(a, b):
    # Функция вычисления суммы двух чисел
    result = a + b
    print(f"Сумма {a} + {b} = {result}")
    return result


# Тестируем работу декорированных функций
if __name__ == '__main__':
    print("Тест функции приветствия:")
    greet_result = greet("Аня")
    print(f"Результат: {greet_result}")


    print("Тест функции вычисления:")
    calc_result = calculate_sum(15, 25)
    print(f"Результат: {calc_result}")