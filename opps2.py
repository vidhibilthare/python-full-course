# instanse methods
# l=[1,2,3]
# l.pop()#method
# print(l)

# class k ander jitne b functions 
# hote hain unko method kehty hain

class Person:
    def __init__(self,name,surname,age):
        #instance variables
        self.name = name
        self.surname = surname
        self.age = age
    def full_name(self):
        return f"{self.name} {self.surname}"
    
    def is_above_18(self):
        return self.age>18

p1 = Person('vidhi','bilthare',26)
p2 = Person('shubhi','shukla',28)
# print(p2.full_name())
print(Person.full_name(p1))
print(p1.is_above_18())

# l=[1,2,3]
# # clear,pop
# l.clear()
# print(l)

# # clear
# list.clear(l)
# print(l)

# l.append(10)
# list.append(l,10)
# print(l)