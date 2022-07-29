from errno import ENOMSG


class Engine:
    a = 10
    def __init__(self):
        self.b = 20
    def m1(self):
        print("Engine specific functionality")
class Car:
    def __init__(self):
        self.engine = Engine()
    def m2(self):
        print("car using engine class functionality")
        print(self.engine.a)
        print(self.engine.b)
        self.engine.m1()
c = Car()
c.m2()