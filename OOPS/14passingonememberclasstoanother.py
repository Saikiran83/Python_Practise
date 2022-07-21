# passing one members of class to another class

class employee:
    def __init__(self,name,age,salary):
        self.name = name 
        self.age = age 
        self.salary = salary
    def display(self):
        print("my name is {}, my age is {}, my salary is {}".format(self.name,self.age,self.salary))
        #return "my name is {}, my age is {}, my salary is {}".format(self.name,self.age,self.salary)
class test:
    def modify(emp):
        emp.salary = emp.salary + 1000
        emp.display()
e = employee('sai',25,100)
e.display()  # no need of print, we r printing in fn itself, if we print we will get 
#print statement and also none 
#print(e.display()) # in function if we return then we need to print here 
test.modify(e)