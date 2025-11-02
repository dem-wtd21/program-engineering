class Transport:
    def move(self):
        pass

class Car(Transport):
    def move(self):
        print("Машина едет по дороге")

class Airplane(Transport):
    def move(self):
        print("Самолет летит в небе")

class Ship(Transport):
    def move(self):
        print("Корабль плывет по морю")

# Разные виды транспорта
transports = [Car(), Airplane(), Ship()]

# Каждый транспорт движется по-своему
for transport in transports:
    transport.move()