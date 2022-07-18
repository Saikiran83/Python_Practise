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
    # @classmethod
    # def fromstr(cls,string):
    #     params = string.split("-")
    #     return cls(params[0],params[1],params[2])
    @classmethod
    def fromstr(cls,string): # used as alternate constructor, gives ip diff 
        return cls(*string.split("-"))
sai = Employee('sai',25,'analyst')
kiran = Employee.fromstr("kiran-25-frontend") 
print(kiran.occupation)
print(sai.occupation)