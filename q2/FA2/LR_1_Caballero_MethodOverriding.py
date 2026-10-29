# Parent class
class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(self.name, "is eating.")

    def sleep(self):
        print(self.name, "is sleeping.")

    def make_sound(self):
        print(self.name, "makes a sound")


#child class
class Lion(Animal):
    def make_sound(self):
        return f"{self.name} roars loudly!"

    def feed(self):
        return f"{self.name} eats fresh meat."

class Elephant(Animal):
    def make_sound(self):
        return f"{self.name} trumpets!"

    def feed(self):
        return f"{self.name} eats grass and fruits."

class Monkey(Animal):
    def make_sound(self):
        return f"{self.name} chatters!"

    def feed(self):
        return f"{self.name} eats bananas."

lion = Lion("Simba")
elephant = Elephant("Dumbo")
monkey = Monkey("George")

animals = [lion, elephant, monkey]

for animal in animals:
    print(animal.make_sound())
    print(animal.feed())
    print("-----")

