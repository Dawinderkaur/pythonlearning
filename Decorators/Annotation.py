#-------------------------------Annotations--------------------------------------
# in Python are a way to attach metadata to function arguments and return values.
# These annotations are optional and do not affect the behavior of the program, but they provide useful information
# that can be utilized by tools, linters, and IDEs.
# Annotations can improve the clarity and readability of code, especially in large projects.


#---------------------------1. Function Argument Annotation--------------------------
#annotate the parameters of a function to indicate the expected type or provide additional information about the argument

#Syntax
#def function_name(param1: type, param2: type) -> return_type:
#    pass

def add1(a: int, b: int) -> int:
    return a + b
#-> int indicates that the return type of the function is an integer.


#################################################################################################

#----------------------------2. Return type Annotation-------------------------------------
#Annotations can also be used to specify the return type of function.

#syntax
#def function_name() -> return_type:
#    pass

def greet(name: str) -> str:
    return "Hello " + name

#-> str indicates that the function greet() will return a string.

#################################################################################################

#----------------------------3. Accessing Annotations--------------------------------------------
#You can access the annotations of a function using the `__annotations__` attribute,
# which returns a dictionary where the keys are the parameter names (and `'return'` for the return type),
# and the values are the corresponding annotations.

#Example:
def add(a: int, b: int) -> int:
    return a + b

print(add.__annotations__) # Output: {'a': <class 'int'>, 'b': <class 'int'>, 'return': <class 'int'>}

#################################################################################################

#--------------------------------------4. Using Any Type---------------------------------------------------
#The `Any` type from the `typing` module allows you to specify that a parameter or return type can be of any type.

# Example:
from typing import Any

def display(value: Any) -> None:
    print(value)

#Here, `Any` means the function can accept any type of argument.

#################################################################################################

#----------------------------5. Other Common Annotations------------------------------------------------------
#Python’s `typing` module provides various predefined types and tools for more complex annotations, such as:

# - **`Optional`**: Indicates that a value can be of a specified type or `None`.
# - **`List`**: Represents a list of elements of a specific type.
# - **`Dict`**: Represents a dictionary with keys and values of specific types.
# - **`Tuple`**: Represents a tuple with a fixed number of elements of specific types.
# - **`Union`**: Indicates that a value can be one of several types.

# Examples:
from typing import List, Dict, Tuple, Optional, Union

# List of integers
def sum_numbers1(nums: List[int]) -> int:
    return sum(nums)

# Dictionary with string keys and integer values
def get_student_info() -> Dict[str, int]:
    return {"John": 10, "Jane": 15}

# Tuple with a string and an integer
def person_info() -> Tuple[str, int]:
    return "Alice", 30

# Optional value that could be an integer or None
def find_item(item: Optional[int]) -> str:
    return f"Found item {item}" if item is not None else "Item not found"

# Union of two possible types
def add_value(value: Union[int, float]) -> float:
    return value + 5.0


##############################################################################################################

#---------------------------------------6. Type Aliases------------------------------------------------------
# You can create custom type aliases for more complex types.

# Example:
from typing import List

# Create a type alias for a list of integers
IntList = List[int]

def sum_numbers(nums: IntList) -> int:
    return sum(nums)


################################################################################################################

#----------------------------------7. Callable Type Annotations---------------------------------------------------
#If you want to annotate a function type (i.e., a function that takes a specific
# set of arguments and returns a particular type), you can use `Callable`.

# Example:
from typing import Callable

def process(callback: Callable[[int, int], int]) -> int:
    return callback(3, 5)

# Define a function matching the Callable annotation
def add(a: int, b: int) -> int:
    return a + b

print(process(add))  # Output: 8

#################################################################################################################

#--------------------------------------------------Summary---------------------------------------------------------
# - Annotations provide a way to add metadata about the types of function arguments and return values.
# - They are optional and do not affect the runtime behavior.
# - Annotations are typically used for better code clarity and tools like linters, IDEs, and type checkers (e.g., mypy)
# can leverage these annotations to catch errors and provide more accurate suggestions.
# - Python's `typing` module provides rich support for advanced annotations like `List`, `Dict`,
# `Union`, `Optional`, `Callable`, and more.
