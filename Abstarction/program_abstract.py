#-----------------Abstraction---------------
#It is the process of hiding implementation details and showing only the necessary features of an object
#Abstract Class - is designed to be a blueprint for other subclasses
#Abstract class is a class that cannot be instantiated on its own
#abstraction is implemented using abstract classes and abstract methods,
# which are provided by the abc (Abstract Base Class) module.

#---------------Abstract Base Class in python -----------------
from abc import ABC, abstractmethod #abc module
class Animal(ABC):# Define an abstract class

    @abstractmethod
    def sound(self):
        pass  # This is an abstract method, no implementation here.

class Dog(Animal):

    def sound(self):
        return "Bark"  # Providing the implementation of the abstract method

# Create an instance of Dog
dog = Dog()
print(dog.sound())  # Output: Bark

#Abstract Base Class : Animal is an abstract base class inherit from ABC. this class
#cannot be initiated because it contains abstract method. Any Subclass can use this method and initiate it.

#Abstract Method - are the functions defined in Abstract class and are not implemented
# these methods act as a blueprint for subclass method and subclass can decide how to implement abstract method

#Concreate Method - are the functions that are fully implemented in Abstract class and subclasses can directly use it
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass  # Abstract method, to be implemented by subclasses

    def move(self):
        return "Moving" #concreate class with implementation

# Why do we use abstract base classes (ABC) in Python?
#
# To define a common interface for multiple classes.
# To ensure that all derived classes implement specific methods.
# To prevent instantiation of an incomplete class (forces subclasses to implement missing functionality).
# Helps in designing a scalable and modular system.