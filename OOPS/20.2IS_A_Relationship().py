class Person:
    def __init__(self,name,age):
        self.name = name 
        self.age = age 
    def eat_drink(self):
        print("{} eat less and drink less".format(self.name))
class Employee(Person):
    def __init__(self, name, age,eno,esal):
        super().__init__(name, age)
        self.eno = eno
        self.esal = esal
    def work(self):
        print("employee works well")
    def employeedetails(self):
        print("Employee Name:",self.name) 
        print("Employee Age:",self.age) 
        print("Employee Number:",self.eno) 
        print("Employee Salary:",self.esal) 
e=Employee('sai', 25, 100, 10000) 
e.eat_drink() 
e.work() 
e.employeedetails()
