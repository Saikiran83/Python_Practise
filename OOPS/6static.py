# We can delete static variables by using only classname or in class variable 
""" If we change the value of static variable by using either self or object reference variable, 
then the value of static variable won't be changed, just a new instance variable with that 
name will be added to that particular object """
class Test:
    x=10
    a=10    
    def __init__(self): 
        self.y=20 
    def m1(self): 
        self.a=888 
t1=Test() 
t1.m1() 
print(Test.a) 
print(t1.a) 
t3=Test() 
t4=Test() 
print('t3:',t3.x,t3.y) 
print('t4:',t4.x,t4.y) 
t3.x=888 
t3.y=999 
print('t3:',t3.x,t3.y) 
print('t4:',t4.x,t4.y)
""" Output
10
888 """

 
 