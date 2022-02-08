# if value of variables varied from object to object > those variables > instance variables
# For every object a separate copy of instance variables will be created.
""" Where we can declare Instance Variables:
1) Inside Constructor by using self variable
2) Inside Instance Method by using self variable
3) Outside of the class by using object reference variable """
#1) Inside Constructor by using Self Variable:
""" We can declare instance variables inside a constructor by using self keyword. Once we 
creates object, automatically these variables will be added to the object. """
class Employee:    
    def __init__(self): 
        self.eno=100 
        self.ename='Durga' 
        self.esal=10000 
e=Employee() 
print(e.__dict__) 
#Output: {'eno': 100, 'ename': 'Durga', 'esal': 10000}
#2) Inside Instance Method by using Self Variable:
""" We can also declare instance variables inside instance method by using self variable. If 
any instance variable declared inside instance method, that instance variable will be 
added once we call taht method. """
class Test:  
    def __init__(self): 
        self.a=10 
        self.b=20  
    def m1(self):  
        self.c=30  
t=Test() 
t.m1() 
print(t.__dict__) 
#Output: {'a': 10, 'b': 20, 'c': 30}
#3) Outside of the Class by using Object Reference Variable:
#We can also add instance variables outside of a class to a particular object.
class Test:  
    def __init__(self): 
        self.a=10 
        self.b=20 
    def m1(self): 
        self.c=30 
t=Test() 
t.m1() 
t.d=40 
print(t.__dict__) 
#Output {'a': 10, 'b': 20, 'c': 30, 'd': 40}
""" How to Access Instance Variables:
We can access instance variables with in the class by using self variable and outside of the 
class by using object reference. """
class Test:  
    def __init__(self): 
        self.a=10 
        self.b=20 
    def display(self): 
        print(self.a) 
        print(self.b)  
t=Test() 
t.display() 
print(t.a,t.b) 
""" 
Output
10
20
10 20 """
