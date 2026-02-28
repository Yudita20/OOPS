class Vehicle:
    def __init__(self,name,color,no_of_tires,fuel_level):
        self.name = name
        self.color = color
        self.no_of_tires = no_of_tires
        self.fuel_level = fuel_level

    def start(self,fuel_level):
        if self.fuel_level > 0:
            print(f"Start the.....{self.name}")
        else:
            print("Not enough fuel level")

class Car(Vehicle):
    def __init__(self,name,color,no_of_tires,fuel_level,no_of_doors):
        super().__init__(name,color,no_of_tires,fuel_level)
        self.no_of_doors = no_of_doors

    def start(self,fuel_level):
        if self.fuel_level > 0:
            print(f"Start the .....{self.name}")
        else:
            print(f"Not enough fuel level to run a {self.name}")

royal_enfield = Vehicle("Royal Enfield","Blue", 2, 12)
royal_enfield.start(royal_enfield.fuel_level)

thar = Car("Thar","White",4,12,3)
thar.start(thar.fuel_level)


