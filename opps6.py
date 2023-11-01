# clss methods
# difference b\w clss methods and instance variables

class Person:
    count_instance=0 #class variable/class attributes
    def __init__(self,name,surname,age):
        Person.count_instance+=1
        self.name =name
        self.surname =surname
        self.age =age

    @classmethod
    def count_instances(cls):
        return f"you have created {cls.count_instance} instances of {cls.__name__} class"

    
    def full_name(self):
        return f"{self.name} {self.surname}"
    
    def is_above_18(self):
        return self.age>18

p1 = Person('vidhi','bilthare',26)
p2 = Person('yash','shukla',23)
print(Person.count_instances())
print(p1.count_instances())
