#Inheritance allows us to define a class that inherits all the methods and properties from another class.
#Parent class is the class being inherited from, also called base class.
#Child class is the class that inherits from another class, also called derived class.

#-------------Single Inheritance with pass keyword ---------------------
class Person: #Parent Class
  def __init__(self, fname, lname):
    self.firstname = fname #instance vriable
    self.lastname = lname

  def printname(self): #instance method
    print(self.firstname, self.lastname)

class Student(Person): #Child Class
  pass #pass keyword is used when class is empty (no attributes or method)

x = Student("Mike", "Olsen")
x.printname()

##################################################################################################

#--------Add inherited properties to a child class using __init__() function from parent class-------

#When you add the __init__() function in child class, the child class will no longer inherit the parent's __init__() function.
#Note: The child's __init__() function overrides the inheritance of the parent's __init__() function.
#To keep the inheritance of the parent's __init__() function, add a call to the parent's __init__() function:
class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

class Student(Person):
    def __init__(self, fname, lname):
        Person.__init__(self, fname, lname)

x = Student("Mike", "Olsen")
x.printname()

##########################################################################################

#------------------------Super function--------------------
# will make the child class inherit all the methods and properties from its parent:
#By using the super() function, you do not have to use the name of the parent element, it will automatically inherit the methods and properties from its parent.
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname) # Call the parent class constructor

x = Student("Mike", "Olsen")
x.printname()

##########################################################################################

#----------Add properties and method to child class-----------
class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year #properties of child class

    def welcome(self): #instance method of child class
        print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

x = Student("Mike", "Olsen", 2025)
x.welcome()

#############################################################################################

#----------------------------Multiple inheritance-------------------------------
# Python allows a class to inherit from more than one class.
# In this case,
# the method resolution order (MRO) determines the order in which the base classes are inherited.
class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

class Studies:
    def __init__(self, course):
        self.coursename = course

    def printcoursename(self):
        print(self.coursename)

class Student(Person, Studies):
    def __init__(self, fname, lname, course, year):
        # Initialize both parent classes using super()
        super().__init__(fname, lname)
        Studies.__init__(self, course)  # Explicitly call the constructor of Studies
        self.graduationyear = year

    def welcome(self): #instance method of child class
        print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear, "in", self.coursename)

x = Student("Mike", "Olsen", "BTech", 2025)
x.welcome()

##########################################################################################

#--------------------Overriding Method ---------------------------------
#override methods from the parent class in the child class is used to modify the behavior.
# This is helpful when you want to provide a different implementation.
class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year #properties of child class

    def printname(self): #overriding method
        print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

x = Student("Mike", "Olsen", 2025)
x.printname()

################################################################################
#-----------------------------Inheritance Class Method -----------------------------
class Person:
    @classmethod
    def printname(cls):
        print("I am Mike Olsen")

class Student(Person):
    @classmethod
    def printname(cls): #overiding
        print("Welcome to College Mike Olsen") #overriding method

x = Student
x.printname()

##################################################################################
#--------------------Inheritance from built-in type -----------------------------
class MyList(list): #inheritance from in built list
    def append(self, item): #method
        if isinstance(item, int): #condition
            super().append(item)

lst = MyList()
lst.append(5)  # Works fine
lst.append("hello")  # Does not append due to check
print(lst)  # Output: [5]
