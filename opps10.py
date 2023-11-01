# will discuss three problems in existing
# then we will solve them using getter , setter decorator

class Phone:
    def __init__(self,brand,model,price):
        self.brand = brand
        self.model = model
        if price > 0 :
             self.price = price  
        else:
            self.price = 0
            
        # self.complete_specification = f"{self.brand} {self.model} and price is {self.price}"
    @property
    def complete_specification(self):
        return (f"{self.brand} {self.model} and price is {self.price}")

    # getter(),setter() (for change price)
    # @property
    # def price( self):
    #     return self.price

    # @price.setter
    # def price(self,new_price):
    #     self.price = max(new_price,0)


    def make_a_call(self,phone_number):
        print(f"calling {phone_number}..")

    def full_name(self):
        return f"{self.brand} {self.model}"
    
phone1 =Phone('nokia','1100',1000)
print(phone1.brand)
print(phone1.model)
phone1.price = 500
print(phone1.price)
print(phone1.complete_specification)



# sakshivaishnav@thoughtwin.com