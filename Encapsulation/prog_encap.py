#-----------------------Encapsulation----------------------------
# Encapsulation is the process of wrapping data (variables) and methods (functions) into a single unit (class)
# and restricting direct access to some of an object's components.

#Example - Bank Account system
# where your account balance (data) is kept private.
# You can’t directly change your balance by accessing the account database.
# Instead, the bank provides you with methods (functions) like deposit and withdraw to modify your balance safely.

# Key Benefits of Encapsulation:
# ✅ Data Protection – Prevents accidental modification of data.
# ✅ Code Maintainability – Reduces dependency between different parts of the program.
# ✅ Security – Sensitive data is hidden from direct access.
# ✅ Flexibility – Provides controlled access to data through getter and setter methods.

#Access Modifier in Python
#1. Public - No restriction - self.name - Accessed Anywhere
#2. Protected - can be accessed but should be cautiously - _name - inside class & subclasses
#3. Private - strictly restricted access - __name - only inside the class

##############################################################################################
#------------------Public Members--------------------
class Student:
    def __init__(self, name, age):
        self.name = name #public attribute
        self.age = age #public attribute

    def display(self):
        print(f"Student Name: {self.name}, Age: {self.age}")

s = Student("John", 20)
s.display()

#Public members can be accessed directly
print(s.name) #John
s.age = 25
print(s.age)  #25

#Public members can be accessed and modified directly.

#############################################################################################
#------------------------Protected Members(_variable)----------------
class Student:
    def __init__(self, name, age):
        self._name = name   # Protected attribute
        self._age = age     # Protected attribute

    def _display(self):  # Protected method
        print(f"Student Name: {self._name}, Age: {self._age}")

class CollegeStudent(Student):
    def show(self):
        print(f"Accessing protected name: {self._name}")

s = CollegeStudent("Alice", 22)
s.show()  # Accessing protected name: Alice

# Technically accessible, but not recommended
# print(s._name)  # Alice

#Protected members are not strictly private but indicate that they shouldn't be accessed outside the class hierarchy.

#############################################################################################
#------------------------Private Members(__variable)----------------
class Student:
    def __init__(self, name, age):
        self.__name = name  # Private attribute
        self.__age = age    # Private attribute

    def display(self):
        print(f"Student Name: {self.__name}, Age: {self.__age}")

s = Student("Emma", 21)
s.display()

# Attempting to access private members directly will cause an error
# print(s.__name)  # AttributeError

#Private members are name-mangled and cannot be accessed directly.

#Bypassing encapsulation through - Name Mangling (Not Recommended)
# print(s._Student__name). #Emma

###############################################################################################################
#---------------------Accessing Private attributes through Getter & Setter-------------------------
class Student:
    def __init__(self, name, age):
        self.__name = name  # Private attribute
        self.__age = age    # Private attribute

    # Getter method
    def get_name(self):
        return self.__name

    # Setter method
    def set_name(self, new_name):
        self.__name = new_name

s = Student("Oliver", 23)
print(s.get_name())  # Oliver

s.set_name("Sophia")
print(s.get_name())  # Sophia

