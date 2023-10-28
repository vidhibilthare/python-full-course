# objective
# what is classs
# how to create an classs
# what is init methods-->(constructor)
# what are attribute and instance variable
# how to create our objects


class Person:
    def __init__(self,first_name,last_name,age):
        # instance_variables
        print("init method\\constructor get called")
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
p1 = Person('vidhi','bilthare',26)
p2 = Person('himanshu','bilthare',28)
print(p1.first_name)
print(p2.first_name)

    