# resolution order


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
    
    def full_name(self):
        return f"{self.brand} {self.model} and price is {self.price} ."

class Flagshiphone(Smartphone):
     def __init__(self,brand,model,price,rem,internal_memory,rear_camera,front_camera):
         super().__init__(brand,model,price,rem,internal_memory,rear_camera)
         self.front_camera = front_camera
        
     def full_name(self):
        return f"{self.brand} {self.model} and price is {self.price} and front camera {self.front_camera}."

# phone = Phone('nokia','1100',1000)
smartphone = Smartphone('oneplus','ce2lite',30000,'6gb','256gb','8mp')
oneplus = Flagshiphone('oneplus','ce3lite',30000,'6gb','256gb','8mp','30mp')
print(oneplus.full_name())
# print(help(smartphone))