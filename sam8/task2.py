class Book:
    def __init__(self, title, author, pages, genre):
        self.title = title
        self.author = author
        self.pages = pages
        self.genre = genre
        self.is_read = False

    def read_book(self):
        self.is_read = True
        print(f"Книга '{self.title}' прочитана!")

    def book_status(self):
        status = "прочитана" if self.is_read else "не прочитана"
        print(f"Статус книги: {status}")

    def full_info(self):
        print(f"'{self.title}' - {self.author}")
        print(f"Жанр: {self.genre}, Страниц: {self.pages}")
        self.book_status()


# Создание объекта и работа с методами
my_book = Book("1984", "Джордж Оруэлл", 384, "роман-антиутопия")
my_book.full_info()
print("---")
my_book.read_book()
my_book.book_status()