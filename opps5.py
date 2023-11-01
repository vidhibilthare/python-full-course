class Laptop:
    discount_percent = 10  # Class-level variable for the discount percentage

    def __init__(self, brand, model, price):
        # Instance variables
        self.brand = brand
        self.model = model
        self.price = price
        self.laptop_name = brand + ' ' + model

    def apply_discount(self):
        # Calculate the discounted price
        off_price = (self.discount_percent / 100) * self.price
        return self.price - off_price

# Set the discount percentage for all laptops to 0 (no discount)
# Laptop.discount_percent = 100

laptop1 = Laptop('hp', 'i5', 55000)
laptop2 = Laptop('dell', 'i5', 75000)
laptop2.discount_percent = 50


# Now you can apply the discount to the laptops
discounted_price1 = laptop1.apply_discount()
discounted_price2 = laptop2.apply_discount()
print(discounted_price2)
print(laptop2.__dict__)


