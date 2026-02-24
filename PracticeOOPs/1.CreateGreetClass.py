# Create a class Greeter with a method greet(name) that prints a greeting for the provided name.


class Greeter:
    def __init__(self,name):
        self.name = name

    def greet(self,name):
        print(f"Hello {self.name}")


g = Greeter("GeeksForGeeks")
g.greet("GeeksForGeeks")