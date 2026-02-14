class Atm:
    # Constructor(Method,code automatically executes when called the object of this class)
    # One of the magic/dunder function
    # Used when all the control is on developer not on user
    def __init__(self):
        # Self? Self is the current object only
        # No two function can interact with each other,that's why we use object(self) to do that work
        self.pin = ""
        self.balance = 0
        self.menu()

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



union = Atm()
union.menu()


