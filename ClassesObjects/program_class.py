#Python is an object-oriented programming
# Almost everything is python is object with its properties and methods
# A class is like an object constructor - or bluprint of creating object

class MyClass:
    x = 5

print(MyClass)

###########################################################################

#create object of p1
p1 = MyClass()
print(p1.x)

###########################################################################

#-------------------__init__() function----------------- :
#All classes have a function called __init__(), which is always executed when the class is being initiated.
#Use the __init__() function to assign values to object properties, or other operations that are necessary to do when the object is being created:

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("John", 36) #p1 object created
print(p1.name)
print(p1.age)

###########################################################################

#--------------__str__() function -----------------
#The __str__() function controls what should be returned when the class object is represented as a string.
#without __str__ usage
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p2 = Person("John", 36)

print(p2)


#with __str()__ usage

class Person:
  def __init__(self, name, age):
    self.name = name #instance variable - Unique to each instance, defined using self
    self.age = age #instance variable

  def __str__(self):
    return f"{self.name},{self.age}"

p3 = Person("John", 36)

print(p3)

###########################################################################

#-------------------instance vs class variable-------------------
class Employee:
    company = "TechCorp"  # Class variable (shared) - Shared among all instances of a class.

    def __init__(self, name, age):
        self.name = name  # Instance variable -Unique to each instance, defined using self
        self.age = age    # Instance variable

# Creating instances
emp1 = Employee("Alice", 30)
emp2 = Employee("Bob", 28)

print(emp1.company)  # Output: TechCorp
print(emp2.company)  # Output: TechCorp

# Modifying the class variable
Employee.company = "NewCorp"

print(emp1.company)  # Output: NewCorp
print(emp2.company)  # Output: NewCorp

###########################################################################

#Instance method vs class method vs static method:

#------------instance method-----------:
#Operate on instance variables.  and Use self as the first parameter.
class Dog:
    def __init__(self, name, breed):
        self.name = name #instance variable
        self.breed = breed

    def bark(self): #instance method
        print(f"{self.name} says Woof!")

dog1 = Dog("Buddy", "Labrador")
dog1.bark()  # Output: Buddy says Woof!

#-------------class Method---------------:
#Work with class variables instead of instance variables. Use @classmethod decorator and cls as the first parameter.
class Animal:
    species = "Mammal" #class variable

    @classmethod #decorator
    def set_species(cls, new_species): #cls parameter
        cls.species = new_species #use of class variable

print(Animal.species)  #Before change andOutput: Mammal
Animal.set_species("Reptile")    # Change class variable using class method
print(Animal.species)  #After change Output: Reptile

#------------------static method-------------------- :
#Do not operate on instance or class variables. Use @staticmethod decorator.
#Behave like regular functions inside a class.
class MathOperations:
    @staticmethod #decorator
    def add(x, y): #regular function
        return x + y

# Calling a static method
print(MathOperations.add(5, 3))  # Output: 8

#----------------------self parameter------------------:
#The self parameter is a reference to the current instance of the class, and is used to access variables that belong to the class.
#It does not have to be named self, you can call it whatever you like, but it has to be the first parameter of any function in the class
class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name)

p1 = Person("John", 36)
p1.myfunc()
#Use the words mysillyobject and abc instead of self
