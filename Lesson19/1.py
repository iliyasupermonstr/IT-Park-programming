class Human:
    def __init__(self,age,name,height):
        self.age = age
        self.name = name
        self.height = height
        print("I was born here! My name is",name)

    def say_hello_to(self,name_to):
        print("Hello",name_to)

    def tell_about_yourself(self):
        print("Hello,my name is ",self.age)
        print("I am ",self.age,"y. o.")

    def happy_birthday(self):
        print("Today is my birthday!")
        self.age += 1 


print("Iliya")
Iliya = Human(13,"Iliya",160)
Iliya.say_hello_to("Bazitov")

