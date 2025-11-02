class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.__is_available = True  # Приватный атрибут доступности

    def borrow_book(self):
        # Метод для взятия книги
        if self.__is_available:
            self.__is_available = False
            print(f"Книга '{self.title}' взята для чтения")
        else:
            print(f"Книга '{self.title}' уже занята")

    def return_book(self):
        # Метод для возврата книги
        self.__is_available = True
        print(f"Книга '{self.title}' возвращена")

    def show_info(self):
        # Вывод информации о книге и ее доступности
        status = "доступна" if self.__is_available else "занята"
        print(f"'{self.title}' - {self.author} ({status})")


# Создание объекта
my_book = Book("1984", "Джордж Оруэлл")

# Работа с методами
my_book.show_info()
my_book.borrow_book()
my_book.show_info()
my_book.return_book()
my_book.show_info()