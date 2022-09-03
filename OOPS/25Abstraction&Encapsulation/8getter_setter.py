# To implement proper encapsulation in Python, we need to use setters and getters. The primary purpose of using getters and setters in object-oriented programs is to ensure data encapsulation. Use the getter method to access data members and the setter methods to modify the data members.
# In Python, private variables are not hidden fields like in other programming languages. The getters and setters methods are often used when:
# When we want to avoid direct access to private variables
# To add validation logic for setting a value

class student:
    def __init__(self,name,age):
        self.name = name 
        self.__age = age 
    # getter method
    def get_age(self):
        return self.__age
    #setter method
    def set_age(self,age):
        self.__age = age 
s = student('sai',24)
# retrieving age using getter
print("name:",s.name,s.get_age())
#changing age using setter 
s.set_age(25)
# retrieving age using getter
print("name:",s.name,s.get_age())
