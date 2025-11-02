class Car:
    def __init__(self, make, model):
        self.make = make  # Атрибут для производителя автомобиля
        self.model = model  # Атрибут для модели автомобиля

    def drive(self):
        # Метод, который выводит сообщение о движении автомобиля
        print(f"Driving the {self.make} {self.model}")


# Создание объекта класса Car с конкретными параметрами
my_car = Car("Ford", "Focus")

# Вызов метода drive для созданного объекта
my_car.drive()