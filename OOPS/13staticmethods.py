# In general these methods are general utility methods.
# Inside these methods we won't use any instance or class variables.
# Here we won't provide self or cls arguments at the time of declaration.
# We can declare static method explicitly by using @staticmethod decorator
# We can access static methods by using classname or object reference

class DurgaMath:
    @staticmethod
    def add(x,y):
        print("the sum is",x+y)
    @staticmethod
    def product(x,y):
        print("the product is",x*y)  
DurgaMath.add(10,20) 
DurgaMath.product(10,20) 

# Note:
# In general we can use only instance and static methods.Inside static method we can 
# access class level variables by using class name.
# Class methods are most rarely used methods in python.
