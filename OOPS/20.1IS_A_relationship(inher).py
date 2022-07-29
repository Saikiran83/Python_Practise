# What ever variables, methods and constructors available in the parent class by default 
# available to the child classes and we are not required to rewrite. Hence the main 
# advantage of inheritance is Code Reusability and we can extend existing functionality 
# with some more extra functionality
#whatever members & methods present in parent class are available to child class
# hence on child class reference we can call both parent class , child class methods 

# NOTE : similarly varibales also like (__init__)
# EXAMPLE 

class P: 
    a=10 
    def __init__(self): 
        self.b=20 
class C(P): 
    c=30 
    def __init__(self): 
        super().__init__() #===>Line-1 
        self.d=30  
c1=C() 
print(c1.a,c1.b,c1.c,c1.d)  
# if we comment Line-1 then we will get 
# AttributeError: 'C' object has no attribute 'b' (super used for parent class variables )

# NOTE: If we comment Line-1 then variable b is not available to the child class

