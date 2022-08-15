#Super is built in method, which is useful to call the super class constructors, variables, #methods
# in the below method super used to call parent class constructor and display method 
class person:
    def __init__(self,name,age):
        self.name = name 
        self.age = age 
    def display(self):
        print("my name is {},my age is {}".format(self.name,self.age))
class student(person):
    def __init__(self,name,age,rollno,marks):
        super().__init__(name,age)
        self.rollno = rollno
        self.marks = marks 
    def display(self):
        super().display()
        print("roll no",self.rollno)
        print("marks",self.marks)
s = student('saikiran', 23,99,80)
s.display()


