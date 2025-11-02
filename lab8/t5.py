# Основной класс для всех фигур
class Shape:
    def area(self):
        # Общий метод, который будет переопределен в дочерних классах
        pass


# Класс прямоугольника
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        # Метод для расчета площади прямоугольника
        return self.width * self.height


# Класс круга
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        # Метод для расчета площади круга
        return 3.14 * self.radius * self.radius


# Создание массива с фигурами
shapes = [Rectangle(5, 10), Circle(7)]

# Цикл для вывода площадей фигур
for shape in shapes:
    print(shape.area())