class Phone:
    def __init__(self,price,brand,model):
        print("Inside Parent(Phone) Constructor")
        self.price = price
        self.brand = brand
        self.model = model

    def purchase(self):
        print("Purchased the phone")


class SmartPhone(Phone):
    def purchase(self):
        # Accessing parent class method from child class
        super().purchase()


s = SmartPhone(31000,"Samsung",21)
s.purchase()
