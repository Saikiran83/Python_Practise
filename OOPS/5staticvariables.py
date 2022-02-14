""" If the value of a variable is not varied from object to object, such type of variables we 
have to declare with in the class directly but outside of methods. Such types of 
variables are called Static variables.
For total class only one copy of static variable will be created and shared by all objects 
of that class.
We can access static variables either by class name or by object reference. But 
recommended to use class name. """
class Test: 
    x=10 
    def __init__(self): 
        self.y=20  
t1=Test() 
t2=Test() 
print('t1:',t1.x,t1.y) 
print('t2:',t2.x,t2.y) 
Test.x=888 
t1.y=999 
print('t1:',t1.x,t1.y) 
print('t2:',t2.x,t2.y) 
""" Output
t1: 10 20
t2: 10 20
t1: 888 999
t2: 888 20 """

""" Various Places to declare Static Variables:
1) In general we can declare within the class directly but from out side of any method
2) Inside constructor by using class name
3) Inside instance method by using class name
4) Inside classmethod by using either class name or cls variable
5) Inside static method by using class name """
class Test: 
    a=10 
    def __init__(self): 
        Test.b=20 
    def m1(self): 
        Test.c=30 
# @classmethod 
    def m2(cls): 
        cls.d1=40 
        Test.d2=400 
 #@staticmethod 
    def m3(): 
        Test.e=50 
print(Test.__dict__) 
t=Test() 
print(Test.__dict__) 
t.m1() 
print(Test.__dict__) 
Test.m2() 
print(Test.__dict__) 
Test.m3() 
print(Test.__dict__) 
Test.f=60 
print(Test.__dict__)