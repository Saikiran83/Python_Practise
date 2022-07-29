# class inside another class
# Without existing one type of object if there is no chance of existing another type of object,then we should go for inner classes.
# Example: Without existing Car object there is no chance of existing Engine object. Hence 
# Engine class should be part of Car class.
# class Car:
#  .....
#  class Engine:
#     .....
class outer:
    def __init__(self):
        
        print("outer class ")
    class inner:
        def __init__(self):
            print("inner class executed")
        def m1(self):
            print("hi this is method")
o = outer()
i = o.inner()
m = i.m1()
        

