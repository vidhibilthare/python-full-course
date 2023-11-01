# class variables
# circle
# area
# circum
# c = circle(4,3.14)
class Circle:
    pi=3.14
    def __init__(self,redius):
        self.redius = redius
        
    def calc_circumfrance(self):
        return 2*Circle.pi*self.redius
    
c = Circle(4)
c1 = Circle(5)
print(c.calc_circumfrance())