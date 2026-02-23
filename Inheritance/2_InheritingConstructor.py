class Phone:
    def __init__(self,price,brand,model):
        print("Inside Parent(Phone) Constructor")
        self.price = price
        self.brand = brand
        self.model = model

class SmartPhone(Phone):
    # if there is no constructor for child class
    # then it will inherit the parent class
    # constructor
    pass


s = SmartPhone(31000,"Samsung",21)
print(s.price,s.brand,s.model)