# various important points about super 
# Case-1: From child class we are not allowed to access parent class instance variables by 
# using super(), Compulsory we should use self only.
# But we can access parent class static variables by using super().
class P:
    a=10 
    def __init__(self): 
        self.b=20 
class C(P): 
    def m1(self): 
        print(super().a)#valid 
        print(self.b)#valid 
        print(super().b)#invalid 
c=C()      
c.m1()
# Output:
# 10
# 20
# AttributeError: 'super' object has no attribute 'b

# Case-2: From child class constructor and instance method, we can access parent class 
# instance method, static method and class method by using super()
class P: 
    def __init__(self): 
        print('Parent Constructor') 
    def m1(self): 
        print('Parent instance method') 
    @classmethod 
    def m2(cls): 
        print('Parent class method') 
    @staticmethod 
    def m3(): 
        print('Parent static method') 
class C(P): 
    def __init__(self): 
        super().__init__() 
        super().m1()   
        super().m2() 
        super().m3() 
    def m1(self): 
        super().__init__() 
        super().m1() 
        super().m2() 
        super().m3() 
c=C() 
c.m1() 
# Output:
# Parent Constructor
# Parent instance method
# Parent class method
# Parent static method
# Parent Constructor
# Parent instance method
# Parent class method
# Parent static method

# Case-3: From child class, class method we cannot access parent class instance methods 
# and constructors by using super() directly(but indirectly possible). But we can access
# parent class static and class methods.
class P: 
    def __init__(self): 
        print('Parent Constructor') 
    def m1(self): 
        print('Parent instance method') 
    @classmethod 
    def m2(cls): 
        print('Parent class method') 
    @staticmethod 
    def m3(): 
        print('Parent static method')  
class C(P): 
    @classmethod 
    def m1(cls): 
        #super().__init__()--->invalid 
        #super().m1()--->invalid 
        super().m2()  
        super().m3()  
C.m1() 
# Output:
# Parent class method
# Parent static method

# From Class Method of Child Class, how to call Parent Class Instance Methods 
# and Constructors:
class A: 
    def __init__(self): 
        print('Parent constructor')  
    def m1(self): 
        print('Parent instance method')  
class B(A): 
    @classmethod 
    def m2(cls): 
        super(B,cls).__init__(cls) 
        super(B,cls).m1(cls)  
B.m2() 
# Output:
# Parent constructor
# Parent instance method

# Case-4: In child class static method we are not allowed to use super() generally (But in 
# special way we can use)

class P: 
    def __init__(self): 
        print('Parent Constructor') 
    def m1(self): 
        print('Parent instance method') 
    @classmethod 
    def m2(cls): 
        print('Parent class method') 
    @staticmethod 
    def m3():  
        print('Parent static method')  
class C(P): 
    @staticmethod 
    def m1(): 
    #super().m1() #-->invalid 
    #super().m2() #--->invalid 
    #super().m3() #--->invalid  
C.m1() 
# RuntimeError: super(): no arguments
# How to Call Parent Class Static Method from Child Class Static 
# Method by using super():
class A:  
    @staticmethod 
    def m1(): 
        print('Parent static method')  
class B(A): 
    @staticmethod 
    def m2(): 
        super(B,B).m1()  
B.m2() 
# Output: Parent static method

