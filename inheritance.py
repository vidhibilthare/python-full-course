# inheritance intoductions
class Phone:
    def __init__(self,model,brand,price):
        self.brand = brand
        self.model = model
        self.price = price
    def full_name(self):
        return f"{self.brand} {self.model}"
    def make_a_call(self,number):
        return f"calling {number}...."
    
class Smartphone:
    def __init__(self,brand,model,price,ram,internal_memory,rear_camera):
        self.brand = brand
        self.model = model
        self.price = price
        self.ram = ram
        self.internal_memory = internal_memory
        self.rear_camera = rear_camera

    def full_name(self):
        return f"{self.brand} {self.model}"
    
    def make_a_call(self,number):
        return f"calling {number}..."
    
phone  = Phone('nokia','1100',1000)
smartphone = Smartphone('oneplus','ce2lite',30000,'6GB' , '64GB' ,'20MP')
print(phone.full_name())
print(smartphone.full_name())