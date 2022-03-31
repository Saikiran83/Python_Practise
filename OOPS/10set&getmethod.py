""" Setter Method:
setter methods can be used to set values to the instance variables. setter methods also 
known as mutator methods.
Syntax:
def setVariable(self,variable):
 self.variable=variable
 """
"""  Getter Method:
Getter methods can be used to get values of the instance variables. Getter methods also 
known as accessor methods.
Syntax:
def getVariable(self):
 return self.variable """
class Student: 
    def setName(self,name): 
        self.name=name  
    def getName(self): 
        return self.name  
    def setMarks(self,marks): 
        self.marks=marks  
    def getMarks(self): 
        return self.marks  
n=int(input('Enter number of students:')) 
for i in range(n): 
    s=Student() 
    name=input('Enter Name:') 
    s.setName(name) 
    marks=int(input('Enter Marks:')) 
    s.setMarks(marks)  
    print('Hi',s.getName()) 
    print('Your Marks are:',s.getMarks()) 
    print() 