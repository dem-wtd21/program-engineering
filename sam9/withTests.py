class Tomato:
    states = {0: 'отсутствует', 1: 'цветение', 2: 'зеленый', 3: 'красный'}

    def __init__(self, index):
        self._index = index
        self._state = 0

    def grow(self):
        if self._state < 3:
            self._state += 1

    def is_ripe(self):
        return self._state == 3


class TomatoBush:
    def __init__(self, num):
        self.tomatoes = [Tomato(i) for i in range(num)]

    def grow_all(self):
        for tomato in self.tomatoes:
            tomato.grow()

    def all_are_ripe(self):
        return all(tomato.is_ripe() for tomato in self.tomatoes)

    def give_away_all(self):
        self.tomatoes = []


class Gardener:
    def __init__(self, name, plant):
        self.name = name
        self._plant = plant

    def work(self):
        self._plant.grow_all()

    def harvest(self):
        if self._plant.all_are_ripe():
            self._plant.give_away_all()
            print("Урожай собран!")
        else:
            print("Томаты еще не созрели!")

    @staticmethod
    def knowledge_base():
        print("Справка по садоводству: томаты проходят 4 стадии созревания")

Gardener.knowledge_base()

bush = TomatoBush(3)
gardener = Gardener("Джош", bush)


# Тест 1: Вызов справки по садоводству
print("Тест 1: Справка по садоводству")
Gardener.knowledge_base()

# Тест 2: Создание объектов
print("\nТест 2: Создание объектов")
print(f"Создан садовник {gardener.name} с кустом из {len(bush.tomatoes)} томатов")

# Тест 3: Уход за кустом
print("\nТест 3: Уход за кустом")
gardener.work()
print("Садовник поработал с кустом")

# Тест 4: Попытка сбора незрелого урожая
print("\nТест 4: Попытка сбора незрелого урожая")
gardener.harvest()

# Тест 5: Окончательный сбор урожая
print("\nТест 5: Окончательный сбор урожая")
print("Продолжаем ухаживать...")
gardener.work()
gardener.work()
gardener.harvest()
