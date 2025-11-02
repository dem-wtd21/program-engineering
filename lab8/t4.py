class Car:
    def __init__(self, make, model):
        self._make = make  # Защищенный атрибут
        self.__model = model  # Приватный атрибут

    def drive(self):
        # Метод имеет доступ к защищенным и приватным атрибутам
        print(f"Driving the {self._make} {self.__model}")

# Создание объекта класса Car
my_car = Car("Ford", "Focus")
# Доступ к защищенному атрибуту
print(my_car._make)
# Вызов метода drive (работает с защищенными и приватными атрибутами)
my_car.drive()