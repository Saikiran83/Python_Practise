class Student:
    def __init__(self,name,rollno,marks): 
        self.name=name 
        self.rollno=rollno  
        self.marks=marks 

    def talk(self): 
        print("Hello My Name is:",self.name) 
        print("My Rollno is:",self.rollno) 
        print("My Marks are:",self.marks) 
 
s1=Student("Durga",101,80) 
s1.talk()