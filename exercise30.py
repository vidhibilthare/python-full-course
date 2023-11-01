# create a loptop class with attributes like brand name,model name,price
# create two objects / instance of your laptop classs
class Laptop:
    def __init__(self,brand_name,model_name,price):
        #instance variable
        self.brand = brand_name
        self.model = model_name
        self.rate = price
l1 = Laptop('hp','i5',55000)
l2 = Laptop('dell','i3',45000)
print(l1.model)
print(l2.rate)