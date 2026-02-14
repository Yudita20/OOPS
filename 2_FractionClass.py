# This is a basic fraction class that has operations such as add,sub,mul and div

class Fraction:
    # Constructor
    def __init__(self,n,d):
        self.num = n
        self.deno = d

    def __str__(self):
        # Object description
        return f"{self.num}/{self.deno}"

    def __add__(self,other):
        temp_num = (self.num * other.deno) + (self.deno * other.num)
        temp_deno = self.deno * other.deno
        return f"{temp_num}/{temp_deno}"

    def __sub__(self,other):
        temp_num = (self.num * other.deno) - (self.deno * other.num)
        temp_deno = self.deno * other.deno
        return f"{temp_num}/{temp_deno}"

    def __mul__(self, other):
        temp_num = self.num * other.num
        temp_deno = self.deno * other.deno
        return f"{temp_num}/{temp_deno}"

    def __truediv__(self, other):
        temp_num = self.num * other.deno
        temp_deno = self.deno * other.num
        return f"{temp_num}/{temp_deno}"



x = Fraction(3,4)
y = Fraction(5,6)
print(x+y)
print(x-y)
print(x*y)
print(x/y)