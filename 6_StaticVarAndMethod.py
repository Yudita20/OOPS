class Atm:
    # Static Variable
    # Associated with the class and one for all objects in the class
    __counter = 1
    def __init__(self):
        # Instance Variable
        self.pin = ""
        self.balance = 0
        self.sno = Atm.__counter

        Atm.__counter += 1
        # self.menu()

    @staticmethod
    def get_counter():
        return Atm.__counter

    @staticmethod
    def set_counter(new_count):
        if type(new_count) == int:
            Atm.__counter = new_count
        else:
            print("Not allowed")


    def create_pin(self):
        self.pin = input("Enter your pin:")
        print("Pin set successfully")

    def deposit(self):
        temp = input("Enter your pin:")
        if temp == self.pin:
            amt = int(input("Enter the amount:"))
            self.balance += amt
            print("Deposit successfully")
        else:
            print("Invalid pin")


    def withdraw(self):
        temp = input("Enter your pin:")
        if temp == self.pin:
            amt = int(input("Enter the amount:"))
            if amt<self.balance:
                self.balance -= amt
                print("Withdraw successfully")
            else:
                print("Insufficient Balance")
        else:
            print("Invalid pin")

    def check_balance(self):
        temp = input("Enter your pin:")
        if temp == self.pin:
            print("Balance:",self.balance)
        else:
            print("Invalid pin")


    def menu(self):
        user_input = input(""" 
                     hello,how would you like to proceed
                     1.Enter 1 to create pin
                     2.Enter 2 to deposit
                     3.Enter 3 to withdraw
                     4.Enter 4 to check balance
                     5.Enter 5 to exit
                     """)

        if user_input == "1":
            self.create_pin()
        elif user_input == "2":
            self.deposit()
        elif user_input == "3":
            self.withdraw()
        elif user_input == "4":
            self.check_balance()
        else:
            print("EXIT")



c1 = Atm()
c2 = Atm()
c3 = Atm()
# print(c1.sno,c2.sno,c3.sno)
print(Atm.get_counter())
Atm.set_counter("3")
print(Atm.get_counter())



