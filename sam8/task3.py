class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def info(self):
        print(f"Книга: '{self.title}', Автор: {self.author}")


# Класс AudioBook наследуется от Book
class AudioBook(Book):
    def __init__(self, title, author, pages, duration):
        super().__init__(title, author, pages)
        self.duration = duration  # Длительность в часах

    def play(self):
        print(f"Воспроизведение аудиокниги '{self.title}', длительность: {self.duration} часов")


# Создание объекта AudioBook
my_audio = AudioBook("1984", "Джордж Оруэлл", 328, "от 10 до 14")

# Вызов унаследованного метода
my_audio.info()

# Вызов метода класса AudioBook
my_audio.play()