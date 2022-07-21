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
class programmer(Employee):
    def __init__(self,name,salary,occupation,language):
        self.name = name
        self.salary = salary
        self.occupation = occupation
        self.language = language
    def printprogram(self):
        return f"his name is {self.name}, his salary is {self.salary}, his good at  is {self.language}, "

sai = Employee('sai',12000,'analyst')
kiran = programmer('sai',15000,'fullstackdatascientist','Pythonand dsa')
sai.details()
print(kiran.printprogram())

