#Type of Decorators
#1. Function Decorators
#2. Method Decorators
#3. Class Decorators
#4. Chaining Decorators
#5. Function Wrapper
#6. Built-in Decorators - static method, class method, property decorator

###############################################################################################
#--------------------------1. Function Decorator ----------------------------

#The most common type of decorator, which takes a function as input and returns a new function.
def simple_decorator(func):
    def wrapper():
        print("Before calling the function.")
        func()
        print("After calling the function.")
    return wrapper

@simple_decorator  #Function Decorator
def greet():
    print("Hello, World!")

greet()

#Here, the simple_decorator modifies the greet function to return an wrapper version.

###################################################################################################
#---------------------------2. Method Decorator ---------------------------------

#Used to decorate methods within a class. They often handle special cases, such as the self argument for instance methods.
def method_decorator(func):
    def wrapper(self, *args, **kwargs):
        print("Before method execution")
        res = func(self, *args, **kwargs)
        print("After method execution")
        return res
    return wrapper

class MyClass:
    @method_decorator
    def say_hello(self):
        print("Hello!")

obj = MyClass()
obj.say_hello()

#Output:

#Before method execution
#Hello!
#After method execution

###############################################################################################
#---------------------------------3. Class Decorator ----------------------------------

#These decorators are applied to classes, allowing you to modify or extend the behavior of a class.

def add_class_name(cls):
    cls.class_name = cls.__name__
    return cls

@add_class_name #Class Decorator
class Person:
    pass

print(Person.class_name)  # Output: "Person"

#the add_class_name decorator adds an attribute class_name to the class Person, which stores the class name.

##############################################################################################################
#---------------------------------4. Chaining Decorator(Nested Decorator) ----------------------------------

#Chaining decorators means applying more than one decorator inside a function.
# Python allows us to implement more than one decorator to a function.

#Syntax
# @decor1
# @decor
# def num():
#    statement(s)

#Firstly the inner decorator will work and then the outer decorator.

# code for testing decorator chaining
def decor1(func):
    def inner():
        x = func()
        return x * x
    return inner

def decor(func):
    def inner():
        x = func()
        return 2 * x
    return inner

@decor1
@decor
def num():
    return 10

@decor
@decor1
def num2():
    return 10

print(num()) # 400
print(num2()) # 200


##############################################################################################################
#---------------------------------5. Function Wrapper ----------------------------------

#Function decorators often use wrappers to execute code before or after the function call, or even modify the arguments and return values.

def log_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Calling function {func.__name__} with arguments {args} and {kwargs}")
        result = func(*args, **kwargs)
        print(f"Function {func.__name__} returned {result}")
        return result
    return wrapper

@log_decorator
def add(a, b):
    return a + b

add(2, 3)
# Output:
# Calling function add with arguments (2, 3) and {}
# Function add returned 5


##############################################################################################################
#---------------------------------6. Built-In Decorator ----------------------------------

#Python also provides some built-in decorators such as @property, @staticmethod, and @classmethod.
#@property: Used to define getter, setter, and deleter methods for a class property.

class MyClass:
    @staticmethod
    def greet():
        print("Hello from static method!")

MyClass.greet()  # Output: "Hello from static method!"

class MyClass:
    @classmethod
    def greet(cls):
        print(f"Hello from class method of {cls.__name__}!")

MyClass.greet()  # Output: "Hello from class method of MyClass!"

class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property # get method
    def area(self):
        return self._width * self._height

r = Rectangle(5, 10)
print(r.area)  # Output: 50 (accessing the property like an attribute)
