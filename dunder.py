# special ,agic method/ dunder methods
# operator overloading
# polymorphism

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

# my_phone = Phone('nokia','1100',1000)
# print(str(my_phone)) 
# print(repr(my_phone)) 
my_phone=Phone('nokia','1100',1000)
print(len(my_phone))