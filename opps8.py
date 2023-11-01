# static methods


class Person:
    count_instance=0 #class variable/class attributes
    def __init__(self,name,surname,age):
        Person.count_instance+=1
        self.name =name
        self.surname =surname
        self.age =age

    @classmethod
    def from_String(cls,string):
        first,last,age=string.split(',')
        return cls(first,last,age)


    @classmethod
    def count_instances(cls):
        return f"you have created {cls.count_instance} instances of {cls.__name__} class"

    @staticmethod
    def hello():
        print("hello , static method called...")
    
    def full_name(self):
        return f"{self.name} {self.surname}"
    
    def is_above_18(self):
        return self.age>18

p1 = Person('vidhi','bilthare',26)
p2 = Person('yash','shukla',23)

p3=Person.from_String('vidhi,bilthare,26')
print(p3.full_name())
Person.hello()