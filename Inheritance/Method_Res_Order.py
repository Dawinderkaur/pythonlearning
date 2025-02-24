#---------------MRO / Diamond problem -------------------
#Python uses a method resolution order (MRO) to determine the order in which base classes are inherited.
# If you have multiple inheritance, the MRO becomes critical.
class A:
    def method(self):
        print("A's method")

class B(A):
    def method(self):
        print("B's method")

class C(A):
    def method(self):
        print("C's method")

class D(B, C):
    pass

# Example usage
d = D()
d.method()
#The order in which methods are resolved follows the MRO,
# which can be checked using the mro() method:
print(D.mro())

#In this case, B is preferred over C because
#Python follows the left-to-right order in the method resolution order.