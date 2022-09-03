# If 2 methods have same name but different type of arguements then those methods are said to be overloaded methods
# Python don't support method overloading by default
# If we are trying to declare multiple methods with same name but different type of arguements then python will always consider the latest method only
class Test:
    def m1(self):
        print("no arguement")
    def m1(self,a):
        print("one arguement")
    def m1(self,a,b):
        print("two arg method")
t= Test()
# t.m1() o/p Test.m1() missing 2 required positional arguments: 'a' and 'b'
# t.m1(10) o/p Test.m1() missing 1 required positional argument: 'b'
t.m1(10,15) # consider only latest method 