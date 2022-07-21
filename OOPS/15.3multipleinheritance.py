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
    @staticmethod
    def printdetails(x):
        print("my number is",x)
class player:
    no_of_leaves = 11
    def __init__(self,name,sport):
        self.name = name 
        self.sport = sport 
    def printd(self):
        print("{} plays {} very well".format(self.name,self.sport))
class coolprogrammer(Employee,player): ## if we print no of varibales it'll be 10 because employee is first
    language = 'python'
    def details_1(self):
        print (self.language)
sai = player('sai','cricket')
saiki = coolprogrammer("sai",1400,'analyst')
saiki.details()
saiki.details_1()
