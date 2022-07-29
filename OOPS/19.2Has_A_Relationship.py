# here employee class has a car reference ,so he can access all members of class car
class car:
    def __init__(self,name,model,price):
        self.name = name
        self.model = model
        self.price = price 
    def getinfo(self):
        print("car name:{},model :{},price :{}".format(self.name,self.model, self.price))
class Employee:
    def __init__(self,ename, eno, car):
        self.ename = ename
        self.eno = eno
        self.car = car
    def returninfo(self):
        print("employee name is :",self.ename)
        print("employee no is :",self.eno)
        print("employee car details:")
        self.car.getinfo()
c = car("hyundai", 'creta', 2000000)
e = Employee("saikiran",22232,c)
e.returninfo()