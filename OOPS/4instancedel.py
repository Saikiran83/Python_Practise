
## deletion of instance variables  ###
""" Within a class we can delete instance variable as follows """
# del self.variableName
"""From outside of class we can delete instance variables as follows """
# del objectreference.variableName """
class sai:
    def __init__(self):
        self.a = 10
        self.b = 20
    def m(self):
        del self.b
t = sai()
print(t.__dict__)
t.m()
print(t.__dict__)
del t.a
print(t.__dict__)
#####################################
""" Note: The instance variables which are deleted from one object,will not be deleted from 
other objects.
 """
class Test: 
    def __init__(self): 
        self.a=10 
        self.b=20 
        self.c=30 
        self.d=40  
t1=Test() 
t2=Test() 
del t1.a 
print(t1.__dict__) 
print(t2.__dict__) 
################################
""" If we change the values of instance variables of one object then those changes won't be 
reflected to the remaining objects, because for every object we are separate copy of 
instance variables are available. """
 
class Test: 
    def __init__(self): 
        self.a=10 
        self.b=20  
t1=Test() 
t1.a=888 
t1.b=999 
t2=Test() 
print('t1:',t1.a,t1.b) 
print('t2:',t2.a,t2.b) 
""" Output
t1: 888 999
t2: 10 20

 """
 