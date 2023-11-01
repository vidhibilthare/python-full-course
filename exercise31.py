class Laptop:
    def __init__(self,brand,model,price):
        # instance variables
        self.brand = brand
        self.model = model
        self.price = price
        self.laptop_name = brand+' '+model
    def apply_discount(self,num):
        #self.price
        off_price=num/100*self.price
        return self.price-off_price
    
laptop1 =Laptop('hp','i5',55000)
print(laptop1.laptop_name)
print(laptop1.apply_discount(15))