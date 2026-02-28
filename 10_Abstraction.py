#  Gives idea not the implementation
from abc import ABC,abstractmethod

# Abstract Class
class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    def walk(self):
        print("Dog walks")

    def sound(self):
        print("Bawwwww")

dog = Dog()
dog.sound()