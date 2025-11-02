class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def info(self):
        print(f"Книга: '{self.title}'")
        print(f"Автор: {self.author}")
        print(f"Количество страниц: {self.pages}")


# Создание объекта класса Book
my_book = Book("1984", "Джордж Оруэлл", 384)

# Вызов метода info
my_book.info()