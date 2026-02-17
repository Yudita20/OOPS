# Instance Variable:Variables that are defined in constructor
# and different for different objects

# Nothing in python is truly private
class Atm:
    def __init__(self):
        # private data members (__)
        self.__pin = ""    #_Atm__pin
        self.__balance = 0  #_Atm__balance

    def get_pin(self):
        return self.__pin

    def set_pin(self,new_pin):
        if type(new_pin) == str:
            self.__pin = new_pin
            print("Changed")
        else:
            print("Invalid pin")


    def create_pin(self):
        self.__pin = input("Enter your pin:")
        print("Pin set successfully")

    def deposit(self):
        temp = input("Enter your pin:")
        if temp == self.__pin:
            amt = int(input("Enter the amount:"))
            self.__balance += amt
            print("Deposit successfully")
        else:
            print("Invalid pin")


    def withdraw(self):
        temp = input("Enter your pin:")
        if temp == self.__pin:
            amt = int(input("Enter the amount:"))
            if amt<self.__balance:
                self.__balance -= amt
                print("Withdraw successfully")
            else:
                print("Insufficient Balance")
        else:
            print("Invalid pin")

    def check_balance(self):
        temp = input("Enter your pin:")
        if temp == self.__pin:
            print("Balance:",self.__balance)
        else:
            print("Invalid pin")


    def menu(self):
        while True:
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
                break



union = Atm()
union.menu()
# union.set_pin("1235")
print(union.get_pin())



