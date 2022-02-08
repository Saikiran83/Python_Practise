""" Constructor Concept:
☕ Constructor is a special method in python.
☕ The name of the constructor should be __init__(self)
☕ Constructor will be executed automatically at the time of object creation.
☕ The main purpose of constructor is to declare and initialize instance variables.
☕ Per object constructor will be exeucted only once.
☕ Constructor can take atleast one argument(atleast self)
☕ Constructor is optional and if we are not providing any constructor then python will 
provide default constructor. """

def __init__(self,name,rollno,marks): 
    self.name=name 
    self.rollno=rollno 
    self.marks=marks 

#Program to demonistrate Constructor will execute only once per Object:
class Test: 
    def __init__(self):  
        print("Constructor exeuction...") 
    def m1(self): 
        print("Method execution...") 
t1=Test() 
t2=Test() 
t3=Test() 
t1.m1() 
""" Output
Constructor exeuction...
Constructor exeuction...
Constructor exeuction...
Method execution...
 """
#Program:
class Student:      
 ''''' This is student class with required data''' 
    def __init__(self,x,y,z): 
        self.name=x 
        self.rollno=y 
        self.marks=z 
    def display(self): 
        print("Student Name:{}\nRollno:{} \nMarks:{}".format(self.name,self.rollno,self.marks)) 
s1=Student("Durga",101,80) 
s1.display() 
s2=Student("Sunny",102,100) 
s2.display() 
""" Output
Student Name:Durga
Rollno:101
Marks:80
Student Name:Sunny
Rollno:102
Marks:100 """
""" Differences between Methods and Constructors
Method Constructor
1) Name of method can be any name 
1) Constructor name should be always __init__
2) Method will be executed if we call that 
 method
2) Constructor will be executed automatically at 
 the time of object creation.
3) Per object, method can be called any number 
 of times.
3) Per object, Constructor will be executed only 
 once
4) Inside method we can write business logic 
4) Inside Constructor we have to declare and 
 initialize instance variable """