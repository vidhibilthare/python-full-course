
# polymorphism-many forms

# len function many time uses
# l=[1,2,3]
# t=(1,2,3)
# s="vidhi"
# print(len(l))
# print(len(t))
# print(len(s))

class Phone:
    def __init__(self,brand,model,price):
        self.brand = brand
        self.model = model
        self.price = price
    def phone_name(self):
        return f"{self.brand} {self.model}"

    #str , repr
    def __str__(self):
        return f"{self.brand} {self.model}"

    def __repr__(self):
        return f"{self.brand} {self.model} and price is {self.price}"
    
    def __len__(self):
        return len(self.phone_name())
class Smartphone(Phone):
    def __init__(self,brand,model,price,camera):
        super().__init__(brand,model,price)
        self.camera = camera

    def phone_name(self):
        return f"{self.brand} {self.model} and price is {self.price}"

    def __len__(self):
        return self.price

my_phone=Phone('nokia','1100',1000)
my_phone2=Phone('nokia','1600',1600)
my_smartphone = Smartphone('samsung','22',30000,'5mp')
print(my_smartphone.phone_name())
print(my_phone.phone_name())
print(len(my_phone))