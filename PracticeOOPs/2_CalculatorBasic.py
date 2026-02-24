class Calculator:
    def add(self,num1,num2):
        return num1+num2

    def sub(self,num1,num2):
        return abs(num1-num2)


cal = Calculator()
print("Sum:",cal.add(2,4))
print("Sub:",cal.sub(2,4))


