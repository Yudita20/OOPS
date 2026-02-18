class Customer:
    def __init__(self,name):
        self.name = name

    def __str__(self):
        return f"It is a Customer Class"

# Function
def greet(customer):
    #same as aliasing
    print(id(customer))
    customer.name = "Anna"
    print(customer.name)
    print(id(customer))


# Object Creation
cust = Customer("Anglina")
print(id(cust))
greet(cust)
print(cust.name)


# Objects of a class are also mutable like list,dic and sets
