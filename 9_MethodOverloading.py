import math


# class Area:
#     def area(self,radius):
#         return math.pi * math.pow(radius,2)
#
#     def area(self,length,breadth):
#         return length*breadth
#
# a = Area()
# print(a.area(4))
# print(a.area(8,9))

# TECHNICALLY,THERE'S NO CONCEPT OF METHOD OVERLOADING IN PYTHON BUT
# WE CAN USE THIS CONCEPT USING DEFAULT ARGUMENTS


class Area:
    def area(self,x,y=0):
        if y == 0:
            print(f"Circle={math.ceil(math.pi * math.pow(x,2))}")
        else:
            print(f"Rectangle = {x*y}")

a = Area()
a.area(4)
a.area(8,9)

