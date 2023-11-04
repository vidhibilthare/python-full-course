# raise error example 2
class Mobile:
    def __init__(self,name):
        self.name = name

class MobileStore:
    def __init__(self):
        self.mobiles = []
    
    def add_mobiles(self,new_mobile):
        if isinstance(new_mobile, Mobile):
            self.mobiles.append(new_mobile)
        else:
            raise TypeError('new mobile should be object of mobile classs')
    

oneplus = Mobile('one plus 6')
samsung = 'samsung galaxy 6'
mobostore = MobileStore()
# print(mobostore.mobiles)
mobostore.add_mobiles(oneplus)
mobo_phones=mobostore.mobiles
print(mobo_phones[0].name)
