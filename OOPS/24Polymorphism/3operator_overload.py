
# overloading multiplication operator to work on employee objects

class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
    def __mul__(self,other):
        return self.salary*other.days

class Timesheet:
    def __init__(self,name,days):
        self.name = name 
        self.days = days 
e = Employee('Sai',1600)
t = Timesheet('sai',30)
print("the monthly salary is :", e*t)