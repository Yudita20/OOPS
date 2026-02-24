class Phone:
    def __init__(self,price,brand,model):
        print("Inside Parent(Phone) Constructor")
        self.price = price
        self.brand = brand
        self.__model = model

# Child class cannot inherit private members of parent class
class SmartPhone(Phone):
    pass



s = SmartPhone(31000,"Samsung",21)
# print(s.price,s.brand,s.__model)