class Person:
    count_instance = 0
    def __init__(self,name,surname,age):
        Person.count_instance+=1
        self.name = name
        self.surname = surname
        self.age = age

p1 = Person('vidhi','bilthare',26)
p2 = Person('vidhi','bilthare',26)
p3 = Person('vidhi','bilthare',26)
print(Person.count_instance)