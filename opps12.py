# can we drive more than one class from base classs
# multilevel inheritance
# method resolution order
# method overriding
# isinstance(),issubclass()

class Phone:  #base class / parent class
    def __init__(self,brand,model,price):
        self.brand = brand
        self.model = model
        self.price = max(price,0)

    def full_name(self):
        return f"{self.brand} {self.model}"
    
    def make_a_call(self,number):
        return f"calling {number}.."
    
class Smartphone(Phone): #drived,child class
    def __init__(self,brand,model,price,rem,internal_memory,rear_camera):
        #two ways
        # Phone.__init__(self,brand,model,price) #uncommon way
        super().__init__(brand,model,price)
        self.rem = rem
        self.internal_memory = internal_memory
        self.rear_camera = rear_camera

class Smartphone2(Phone): #drived,child class
    def __init__(self,brand,model,price,rem,internal_memory,rear_camera):
        #two ways
        # Phone.__init__(self,brand,model,price) #uncommon way
        super().__init__(brand,model,price)
        self.rem = rem
        self.internal_memory = internal_memory
        self.rear_camera = rear_camera


phone =Phone('nokia','1100',1000)
smartphone = Smartphone2('oneplus','ce2lite',30000,'6gb','64gb','20mp')
print(phone.full_name())
print(smartphone.full_name() + f"and price is {smartphone.price}")