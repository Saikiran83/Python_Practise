""" Class Methods:
Inside method implementation if we are using only class variables (static variables), 
then such type of methods we should declare as class method.
We can declare class method explicitly by using @classmethod decorator. 
For class method we should provide cls variable at the time of declaration
We can call classmethod by using classname or object reference variable.
 """
class Employee:
    no_of_leaves = 10
    def __init__(self,name,salary,occupation):
        self.name = name
        self.salary = salary
        self.occupation = occupation
    def details(self):
        print("the name is ",self.name)
    @classmethod
    def changeleaves(cls,changeleaves):
        cls.no_of_leaves = changeleaves

sai = Employee('kiran',25,'analyst')
kir = Employee('sai',25,'dev')
print(sai.name,sai.no_of_leaves)  ##kiran 10 is output here
Employee.no_of_leaves = 34 ##here no of leaves changes to 34, but we need to change in class
# by using class we can change with static, class varibales(objects)
kir.changeleaves(26) # we change that with class, static 
print(sai.no_of_leaves)


