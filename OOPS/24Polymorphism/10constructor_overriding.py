# if child class does not contain constructor then parent class 
# constructor will be executed
# From child class constuctor we can call parent class constructor by using super() method.
class Person: 
    def __init__(self,name,age): 
        self.name=name 
        self.age=age 
class Employee(Person): 
    def __init__(self,name,age,eno,esal): 
        super().__init__(name,age) 
        self.eno=eno 
        self.esal=esal  
    def display(self): 
        print('Employee Name:',self.name) 
        print('Employee Age:',self.age) 
        print('Employee Number:',self.eno) 
        print('Employee Salary:',self.esal) 
e1=Employee('Sai',25,872425,26000) 
e1.display() 
e2=Employee('Kiran',25,872426,20000) 
e2.display()