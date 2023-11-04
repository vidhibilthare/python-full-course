# raise error example 1
# NotImplementedError\
# abstract methods

class Animal:
    def __init__(self,name):
        self.name = name

    def sound(self):
        raise NotImplementedError("you have to define this method in subclasses")

class Dog(Animal):
    def __init__(self,name,breed):
        self.breed = breed

    def sound(self):
        return "bhow bhow"

class Cat(Animal):
    def __init__(self,name,breed):
        super().__init__(name)
        self.breed = breed
    def sound(self):
        return "meao meao"

doggi = Dog('boony','pug')
print(doggi.sound())