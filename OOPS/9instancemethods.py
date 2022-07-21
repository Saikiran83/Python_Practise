# instance method use instance variables 
# this used with the help of self variable

class student:
    def __init__(self,name,marks):
        self.name = name 
        self.marks = marks
    def display(self):
        print("Hi",self.name)
        print("your marks are",self.marks)
    def grade(self):
        if self.marks > 80:
            print("first class")
        elif self.marks >=40 and self.marks <= 80:
            print("average student")
        else:
            print("failed")

n = int(input("enter no of students:"))
for i in range(n):
    name = input("enter name")
    marks = int(input("enter marks:"))
    sai = student(name,marks)
    sai.display()
    sai.grade()
