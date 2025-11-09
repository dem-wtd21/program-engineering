class Mammal:
    className = 'Mammal'

class Dog(Mammal):
    species = 'canine'
    sound = 'wow'

class Cat(Mammal):
    species = 'feline'
    sound = 'meow'

dog = Dog()
print(f"Dog is {dog.className}, but they say {dog.sound}")
cat = Cat()
print(f"Cat is {cat.className}, but they say {cat.sound}")