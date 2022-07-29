# we can create any number of classes inside a class 
class person:
    def __init__(self,name):
        self.name = name
        self.db = self.DOB()
    def display(self):
        print("hi this is : ",self.name)
    class DOB:
        def __init__(self):
            self.date = 11
            self.month = 7
            self.year = 1997
        def display(self):
            print("dob is : {}/{}/{}".format(self.date,self.month,self.year))
p =person('sai')
p.display()
x = p.db
x.display()