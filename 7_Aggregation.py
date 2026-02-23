class Address:
    def __init__(self,state,city,pincode):
        self.state = state
        self.city = city
        self.pincode = pincode

    def change_address(self,new_state,new_city,new_pincode):
        self.state = new_state
        self.city = new_city
        self.pincode = new_pincode

class Customer:
    def __init__(self,name,age,address):
        self.name = name
        self.age = age
        self.address = address

    def edit_profile(self,new_name,new_age,new_state,new_city,new_pincode):
        self.name = new_name
        self.age = new_age
        self.address.change_address(new_state,new_city,new_pincode)

add = Address("West Bengal","Kolkata",200010)
cust = Customer("Alice",23,add)
print(cust.name,cust.age,cust.address.state,cust.address.city,cust.address.pincode)
add.change_address("Jharkhand","Jameshdpur",289111)
cust.edit_profile("Natalia",23,"Jharkhand","Jameshdpur",289111)
print(cust.name,cust.age,cust.address.state,cust.address.city,cust.address.pincode)