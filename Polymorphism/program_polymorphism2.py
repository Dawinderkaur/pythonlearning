#Polymorphism type continue
#-----------------------Operator Overloading (Compile time)----------------------------
#Python allows operators like +, -, *, etc., to be overloaded to work with objects.
class ComplexNumber:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.imag + other.imag)

    def __str__(self):
        return f"{self.real} + {self.imag}i"

c1 = ComplexNumber(2, 3)
c2 = ComplexNumber(4, 5)
c3 = c1 + c2  # Calls __add__ method
print(c3)  # 6 + 8i
# In Python, operators like + behave polymorphically, performing addition, concatenation or merging based on the data type.
# The + operator is overloaded to work with objects of the ComplexNumber class.

#####################################################################################
#---------------------------Duck Typing ----------------------------------
#Duck Typing is a dynamic polymorphism technique in Python where the class of an object is less important than the methods it defines.
#"If it looks like a duck and quacks like a duck, it must be a duck."

class Bird:
    def fly(self):
        return "Bird is flying"

class Airplane:
    def fly(self):
        return "Airplane is flying"

class Fish:
    def swim(self):
        return "Fish is swimming"

# Function using Duck Typing
def make_it_fly(entity):
    print(entity.fly())

# Works for both classes that have a fly() method
bird = Bird()
airplane = Airplane()

make_it_fly(bird)      # Bird is flying
make_it_fly(airplane)  # Airplane is flying

# make_it_fly(Fish())  # ERROR! Fish doesn't have a fly() method

#As long as an object has the fly() method, it works—regardless of its class.

####################################################################################
#--------------------------------------Function and Object Polymorphism------------------------
#Functions can be written in a way that they accept different types of objects.
def add(x, y):
    return x + y

print(add(5, 10))        # 15 (integer addition)
print(add("Hello ", "World"))  # Hello World (string concatenation)
print(add([1, 2], [3, 4]))  # [1, 2, 3, 4] (list merging)

#The same function add() works with integers, strings, and lists.