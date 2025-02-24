#---------------------Abstract Properties-----------------------
#---------------------Getter & Setter --------------------------
#Abstract properties in Python are properties that are defined in an abstract class but must be implemented in a subclass.
# They combine abstraction (forcing subclasses to implement a property) with encapsulation (hiding data).
# Python's abc module allows defining abstract properties using the @property decorator along with @abstractmethod.
# Abstract properties can be read-only (getter only) or read-write (getter & setter)
# Use @property @abstractmethod to create an abstract getter.
# Use @property with @abstractmethod @property_name.setter for read-write properties.

#-----------Read-Only Abstract Properties (Getter Only)-------------------
#A read-only abstract property forces subclasses to implement the getter method but does not require a setter.

from abc import ABC, abstractmethod

class Employee(ABC):
    @property
    @abstractmethod
    def salary(self): #Abstract property that must be implemented in subclasses
        pass

class Developer(Employee): #Subclass implementing the abstract property
    def __init__(self, base_salary):
        self._salary = base_salary #private attribute _salary

    @property
    def salary(self): #Getter method for salary
        return self._salary

dev = Developer(70000)
print(dev.salary)# Output: 70000

# Trying to instantiate the abstract class will raise an error
# emp = Employee()  # TypeError: Can't instantiate abstract class Employee with abstract property salary

# Key points from above program
# salary is a read-only abstract property.
# The Employee class cannot be instantiated because it has an abstract property.
# The Developer class must define salary as a property.

##################################################################################################

#--------------------Read-Write Abstract Properties (Getter & Setter)-------------------

from abc import ABC, abstractmethod

class Employee(ABC):# Abstract class
    @property
    @abstractmethod
    def salary(self):   #Abstract Getter
        pass

    @salary.setter
    @abstractmethod
    def salary(self, value):  #Abstract Setter
        pass

class Developer(Employee):# Subclass implementing both getter and setter
    def __init__(self, base_salary):
        self._salary = base_salary  #private attribute can only use in subclass

    @property
    def salary(self): #Getter method for salary
        return self._salary

    @salary.setter
    def salary(self, value): #setter method for salary
        if value < 0:
            raise ValueError("Salary cannot be negative!")
        self._salary = value

# Creating an object of the subclass
dev = Developer(70000)
print(dev.salary)  # Output: 70000

dev.salary = 80000  # Updating the salary
print(dev.salary)  # Output: 80000

# Trying to set a negative salary will raise an error
# dev.salary = -5000  # Raises ValueError: Salary cannot be negative!

##################################################################################
#---------------Abstract Properties with Computed Values----------------

from abc import ABC, abstractmethod

class Shape(ABC): #Abstract class
    @property
    @abstractmethod
    def area(self):  #abstract property of abstract class
        pass

class Rectangle(Shape): #Subclass
    def __init__(self, length, width): #instance method to declare attributes
        self.length = length
        self.width = width

    @property
    def area(self): #inherited property method implementation acc to subclass need
        return self.length * self.width

class Circle(Shape): #subclass
    def __init__(self, radius): #instance method
        self.radius = radius

    @property
    def area(self): #inherited property method implementation acc to subclass need
        return 3.147 * self.radius * self.radius

rect = Rectangle(10, 5)  #object created
cir = Circle(5) #object created

print("Area of Rectangle is:", rect.area)
print("Area of Circle is:", cir.area)

#The property computes the value dynamically instead of storing it.

##########################################################################################
#------------Abstract Class with Constructor and Attributes-------------------
from abc import ABC, abstractmethod

# Abstract class
class Vehicle(ABC):
    def __init__(self, brand): #constructor
        self.brand = brand  # Attribute

    @abstractmethod
    def speed(self):
        pass  # Abstract method

# Subclass
class Car(Vehicle):
    def speed(self):
        return "The car moves at 100 km/h."

# Subclass
class Bike(Vehicle):
    def speed(self):
        return "The bike moves at 80 km/h."

# Creating objects
car = Car("Toyota") #use of attribute defined in abstract class
bike = Bike("Honda")

print(car.brand, "-", car.speed())  # Output: Toyota - The car moves at 100 km/h.
print(bike.brand, "-", bike.speed())  # Output: Honda - The bike moves at 80 km/h.

