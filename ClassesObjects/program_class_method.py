#Class method vs Instance method vs Static method
#Use instance methods when behavior depends on individual objects.
#Use class methods when behavior affects the class as a whole rather than individual instances.
#Use static methods for utility functions that don't need access to class or instance data.

class School:
    school_name = "Greenwood High"  # Class variable

    def __init__(self, student_name, grade):
        self.student_name = student_name  # Instance variable
        self.grade = grade  # Instance variable

    # Instance method (works with instance data)
    def show_details(self):
        print(f"Student: {self.student_name}, Grade: {self.grade}")

    # Class method (works with class variable)
    @classmethod
    def change_school(cls, new_name):
        cls.school_name = new_name

    # Static method (utility function)
    @staticmethod
    def is_adult(age):
        return age >= 18

# Using instance method
student1 = School("Alice", "5th")
student1.show_details()  # Output: Student: Alice, Grade: 5th

# Using class method
School.change_school("Bright Future Academy")
print(School.school_name)  # Output: Bright Future Academy

# Using static method
print(School.is_adult(20))  # Output: True
