# Access modifiers limit access to the variables and methods of a class. Python provides three types of access modifiers private, public, and protected
# Public : accessed anywhere withing and outside of class
# Protected : accessed within the class and its subclasses
# Private : Only within the class 
# below is data hiding using encapsulation / access modifiers 
class Employee:
    def __init__(self,name,project,salary):
        self.name = name  # public 
        self._project = project  #(protected)
        self.__salary = salary    # private
        