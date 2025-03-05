#Decorators - are a powerful and flexible way to modify or extend the behaviour of function or method, without changing their actual code
#Decorators is essentially a function which take another function as an argument and return new function with enhanced functionality
#It is widely used for logging, authentication and memorization

#"Decorators are essentially functions that return other functions"

#Syntax of decorator:
#def decorator_name(func):
#   def wrapper(*arg, **kwargs):
#       Add functionality before the original function call
#       result = func(*arg, **kwargs)
#       Add functionality after the original function call
#       return result
#   return wrapper
#
#@decorator_name
#def function_to_decorate():
#   Original function code
#   pass



# Explanation of Parameters
# 1. decorator_name(func):
#
# decorator_name: This is the name of the decorator function.
# func: This parameter represents the function being decorated.
# When you use a decorator, the decorated function is passed to this parameter.
#
# 2. wrapper(*args, **kwargs):
# wrapper: This is a nested function inside the decorator. It wraps the original function, adding additional functionality.
# *args: This collects any positional arguments passed to the decorated function into a tuple.
# **kwargs: This collects any keyword arguments passed to the decorated function into a dictionary.
# The wrapper function allows the decorator to handle functions with any number and types of arguments.
#
# 3. @decorator_name:
# This syntax applies the decorator to the function_to_decorate function.
# It is equivalent to writing function_to_decorate = decorator_name(function_to_decorate).

#Example

# A simple decorator function
def decorator(func):
    def wrapper():
        print("Before calling the function.")
        func()
        print("After calling the function.")
    return wrapper

# Applying the decorator to a function
@decorator #greet = decorator(greet)
def greet():
    print("Hello, World!")

greet()

#Output
# Before calling the function.
# Hello, World!
# After calling the function.

############################################################################################
#--------------High-Order Function------------------------
#High Order Functions are function which take another function as argument and change or enhance functionality of a existing function
#Decorators are kind of high order functions

# Key Properties of Higher-Order Functions:
# Taking functions as arguments: A higher-order function can accept other functions as parameters.
# Returning functions: A higher-order function can return a new function that can be called later.

#Example
# A higher-order function that takes another function as an argument
def fun(f, x):
    return f(x)

# A simple function to pass
def square(x):
    return x * x

# Using apply_function to apply the square function
res = fun(square, 5)
print(res)  #25

#first function fun is a higher-order function because it takes another function f as an argument and applies it to the value x

###################################################################################
#-----------------------Function as First Class Object -------------------------
#Functions are first-class object in python
#it means function can be treated like any other object such as int, str, lists
#This give function a unique level of flexibility and allows them to be passed around and manipulated

# Role of First-Class Functions in Decorators:
# Decorators receive the function to be decorated as an argument. This allows the decorator to modify or enhance the function’s behavior.
# Decorators return a new function that wraps the original function. This new function adds additional behavior before or after the original function is called.
# When a function is decorated, it is assigned to the variable name of the original function. This means the original function is replaced by the decorated (wrapped) function.

# Assigning a function to a variable
def greet(n):
    return f"Hello, {n}!"

say_hi = greet  # Assign the greet function to say_hi variable
print(say_hi("Alice"))  # Output: Hello, Alice!

# Passing a function as an argument
def apply(f, v):
    return f(v)

res = apply(say_hi, "Bob")
print(res)  # Output: Hello, Bob!

# Returning a function from another function
def make_mult(f):
    def mult(x):
        return x * f
    return mult

dbl = make_mult(2)
print(dbl(5))  # Output: 10

