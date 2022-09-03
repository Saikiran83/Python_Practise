# We can access private members from outside of a class using the following two approaches

# Create public method to access private members
# Use name mangling
class Employee:
    # constructor
    def __init__(self, name, salary):
        # public data member
        self.name = name
        # private member
        self.__salary = salary
    # public instance methods
    def show(self):
        # private members are accessible from a class
        print("Name: ", self.name, 'Salary:', self.__salary)

# creating object of a class
emp = Employee('Jessa', 10000)

# calling public method of the class
emp.show()
# direct access to private member using name mangling
print('Salary:', emp._Employee__salary)
# accessing private data members
print('Salary:', emp.__salary)   #we get below error
# AttributeError: 'Employee' object has no attribute '__salary'