class Brain:
    def say(self):
        print("bwebwebwe")

class Animal:
    def __init__(self, brain = Brain()):
        self.brain = brain

    def say(self):
        self.brain.say()

    def go(self):
        print("Bye")

class DogBrain():
    def say(self):
        print("Гав-Гав")

class CatBrain():
    def say(self):
        print("Mew")

class Cat(Animal):
    def __init__(self,brain = CatBrain()):
        super().__init__(brain)

class Dog(Animal):
    def __init__(self,brain = DogBrain()):
        super().__init__(brain)

Leona = Cat()
Leona.say()
Leona.go()


Sherlok = Dog()
Sherlok.say()
Sherlok.go()

Frankenstein = Dog(brain = CatBrain())
Frankenstein.say()
