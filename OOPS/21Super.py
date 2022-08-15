class A:
    classvar1 = " i am a class varibale in class A"
    def __init__(self):
        self.var1 = "I am inside class A"
        self.classvar1 = " inside class A"
        self.special = 'Special'
class B(A):
    classvar1 = "inside class B"
    def __init__(self):
        super().__init__() # o/p is Inside class B
        self.var1 = " I am inside class B"
        self.classvar1 ="Inside class B"
        #super().__init__() # if i use super after child class constructor then o/p will be
        # inside class A 
a = A()
b = B()
print(b.classvar1)