#--------------------Polymorphism --------------
#The word "polymorphism" means "many forms", and in programming it refers to
#methods/functions/operators with the same name that can be executed on many objects or classes.

#Types of Polymorphism
#1. Method Overriding (Runtime Polymorphism)
#2. Method Overloading (Python's way of using default arguments)
#3. Operator Overloading
#4. Duck Typing
#5. Function and Object Polymorphism

#########################################################################################
#-------------------Method Overriding (Run-time polymorphism) ---------------------
# Method overriding allows a subclass to provide a specific implementation of a method that is already defined in its parent class.
#Occurs when the behavior of a method is determined at runtime based on the type of the object.
class Animal:
    def speak(self):
        return "Animals make sounds"

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

# Creating objects
dog = Dog()
cat = Cat()

# Calling overridden method
print(dog.speak())  # Woof!
print(cat.speak())  # Meow!

#The same method speak() behaves differently for different objects.

##################################################################################################################
#-------------------------------Method Overloading (Compile-time Polymorphism)-------------------------
#Python does not support true method overloading like Java or C++. Instead, it uses default arguments to achieve similar functionality.

#------------------------------
#Method 1 - using default value like c=0
class MathOperations:
    def add(self, a, b, c=0):
        return a + b + c

math = MathOperations()
print(math.add(5, 10))       # 15
print(math.add(5, 10, 20))   # 35


#------------------------------
#Method 2 - use *arg argument to make same function work differently as per arguments
# Function to take multiple arguments
def add(datatype, *args):
    # if datatype is int ,initialize answer as 0
    if datatype == 'int':
        answer = 0
    # if datatype is str initialize answer as ''
    if datatype == 'str':
        answer = ''
    # Traverse through the arguments
    for x in args:
        # This will do addition if the arguments are int. Or concatenation if the arguments are str
        answer = answer + x
    print(answer)

# Integer
add('int', 5, 6)
# String
add('str', 'Hi ', 'Geeks')



#------------------------------
#Method 3 Using Multiple Dispatch Decorator
from multipledispatch import dispatch

# passing two parameter
@dispatch(int, int)
def product(first, second):
    result = first*second
    print(result)

# passing three parameters
@dispatch(int, int, int)
def product(first, second, third):
    result = first * second * third
    print(result)

# you can also pass data type of any value as per requirement
@dispatch(float, float, float)
def product(first, second, third):
    result = first * second * third
    print(result)

# calling product method with 2 arguments
product(2, 3)  # this will give output of 6

# calling product method with 3 arguments but all int
product(2, 3, 2)  # this will give output of 12

# calling product method with 3 arguments but all float
product(2.2, 3.4, 2.3)  # this will give output of 17.985999999999997

#In Backend, Dispatcher creates an object which stores different implementation and on runtime, it selects the appropriate method as the type and number of parameters passed.

