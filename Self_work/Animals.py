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
class Person:
    def __init__(self, brain = Brain()):
        self.brain = brain
    
    def say(self):
        self.brain.say()

    def go(self):
        print("Пока,хорошего дня!")

class DogBrain():
    def say(self):
        print("Гав-Гав")

class CatBrain:
    def say(self):
        print("Mew")
class CowBrain:
    def say(self):
        print("Муууу")

class FrankensteinBrain:
    def __init__(self, brains):
        self.brains = brains
    def say(self):
        for brain in self.brains:
            brain.say()

class PersonBrain:
    def say(self):
        print('Привет,как дела?')
        
class Cat(Animal):
    def __init__(self,brain = CatBrain()):
        super().__init__(brain)

class Dog(Animal):
    def __init__(self,brain = DogBrain()):
        super().__init__(brain)
class Cow(Animal):
    def __init__(self,brain = CowBrain()):
        super().__init__(brain)

class Russian(Person):
    def __init__(self,brain = PersonBrain()):
        super().__init__(brain)




Leona = Cat()
Leona.say()
Leona.go()


Sherlok = Dog()
Sherlok.say()
Sherlok.go()

Murka = Cow()
Murka.say()
Murka.go()

Ivan = Russian()
Ivan.say()
Ivan.go()
