class Customer:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def intro(self):
        print(f"My name is {self.name} and I am {self.age} years old")

    def __str__(self):
        return f"{self.name},{self.age}"

c1 = Customer("Anna",54)
c2 = Customer("Juli",28)
c3 = Customer("Marie",32)

l1 = [c1,c2,c3]
for x in l1:
    x.intro()