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

class ElectricCar(Car):
    def __init__(self, make, model, battery_capacity):
        # Вызов конструктора родительского класса Car
        super().__init__(make, model)
        # Добавление нового атрибута - емкость батареи
        self.battery_capacity = battery_capacity

    def charge(self):
        # Метод для зарядки электромобиля
        print(f"Charging the {self.make} {self.model} with {self.battery_capacity} kWh")

# Создание объекта класса ElectricCar
my_electric_car = ElectricCar("Tesla", "Model S", 75)

# Вызов унаследованного метода drive из класса Car
my_electric_car.drive()

# Вызов метода charge класса ElectricCar
my_electric_car.charge()