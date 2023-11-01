# encapsulation,abstraction,naming convations,name mangling
# in this video we will talk about
# encapsulation
# abstraction
# some special naming convantions
# name mangling , __name (not a convantion)
class Phone:
    def __init__(self,brand,model,price):
        self.brand =brand
        self.model=model
        self.__price = price

    def make_a_call(self,phone_number):
        print(f"calling {phone_number}..")

    def full_name(self):
        return f"{self.brand} {self.model}"
    
    def send_message(self):
        pass

phone1 = Phone('nokia','1100',1000)
# print(phone1._price)
phone1._phone__price = -1000
print(phone1._phone__price)
print(phone1.__dict__)