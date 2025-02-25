#Project: Library Management System
#This project manages books in a library and allows users to borrow and return them.

#Features of the Project
#✔ Uses Encapsulation to protect book data
#✔ Uses Inheritance to create different types of users (Admin & Member)
#✔ Uses Polymorphism for common methods like borrow_book()
#✔ Uses Abstraction with an abstract User class

from abc import ABC, abstractmethod

class User(ABC):  #Abstract class for users
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def display_role(self):
        pass

class Library: #library class (Encapsulation)
    def __init__(self):
        self.__books = {
            "Python Basics": 3,
            "OOP in Python": 2,
            "Data Science": 1
        }  # Private Attribute Dictionary
        self.borrowed_books = {} # Tracks borrowed books per member

    def display_books(self):
        print("\n📚Available Books:")
        for book, count in self.__books.items():
            print(f"   {book}: {count} copies")

    def borrow_book(self, member, book_name):
        if book_name not in self.__books:
            print(f"❌ '{book_name}' is not available in the library.")
            return False

        if self.__books[book_name] > 0:
            if len(self.borrowed_books.get(member.name, [])) < 2: #Borrow limit
                self.__books[book_name] -= 1
                self.borrowed_books.setdefault(member.name, []).append(book_name)
                return True
            else:
                print(f"❌ {member.name} cannot borrow more than 2 books at a time.")
                return False
        else:
            print(f"❌ '{book_name}' is currently out of stock.")
            return False

    def return_book(self, member, book_name):
        if book_name in self.borrowed_books.get(member.name, []):
            self.__books[book_name] += 1
            self.borrowed_books[member.name].remove(book_name)
            print(f"✅ {member.name} returned '{book_name}'.")
        else:
            print(f"❌ {member.name} did not borrow '{book_name}'.")

    def add_book(self, book_name, count=1):
        """Allows admins to add new books safely."""
        if book_name in self.__books:
            self.__books[book_name] += count
        else:
            self.__books[book_name] = count
        print(f"✅ Added {count} copies of '{book_name}' to the library.")


class Member(User): #Inheritance (Polymorphism)
    def __init__(self, name):
        super().__init__(name)

    def borrow_book(self, library, book_name): #method overriding
        if library.borrow_book(self, book_name):
            print(f"📖 {self.name} borrowed '{book_name}'.")

    def return_book(self, library, book_name): #method overriding
        library.return_book(self, book_name)

    def display_role(self):#use of abstract method from abstract class
        print(f"👤 {self.name} is a library Member.")

class Admin(User): #Inheritance (Polymorphism)
    def __init__(self, name):
        super().__init__(name)

    def add_book(self, library, book_name, count=1):
        """Uses Library method to add books safely."""
        library.add_book(book_name, count)

    def display_role(self):
        print(f"🛠 {self.name} is a library Admin")

library = Library()

admin = Admin("Alice")
member = Member("Bob")

admin.display_role()
member.display_role()

library.display_books()

member.borrow_book(library, "Python Basics")
member.borrow_book(library, "OOP in Python")
member.borrow_book(library, "Data Science")  # Should not allow

admin.add_book(library, "Machine Learning", 2)
member.return_book(library, "OOP in Python")

library.display_books()
member.borrow_book(library, "Data Science")


# Encapsulation (Protecting Data)
# The Library class hides book data using a private attribute self.__books.
# This prevents direct modification of book records from outside the class.
# Instead of directly modifying __books, Library provides methods like
# borrow_book(), return_book(), and add_book() to control access safely.
#
# Inheritance (Reusability & Hierarchy)
# The User class is an abstract base class (ABC) that provides a blueprint for Member and Admin.
# Member and Admin inherit from User and provide their own implementations of methods.
# This reduces code duplication and enforces structure.
#
# Polymorphism (Method Overriding)
# Both Member and Admin override the display_role() method from User, implementing it in their own way.
# Member and Admin both use borrow_book() and add_book() differently, but they work in a consistent manner.
#
# Abstraction (Hiding Implementation Details)
# The User class is abstract (ABC), meaning it cannot be instantiated directly.
# It forces child classes (Member, Admin) to implement display_role(), ensuring consistency.



#OOP Concept	Usage in Project
#Encapsulation	Library.__books is private, accessed via methods.
#Inheritance	Member and Admin inherit from User.
#Polymorphism	display_role(), borrow_book(), and return_book() are overridden.
#Abstraction	User is an abstract class, enforcing display_role().