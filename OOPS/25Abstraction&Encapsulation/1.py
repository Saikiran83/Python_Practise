# In abstraction there is no implementation still we declare it .
# class should be derived from abc module and it should inherit ABC class 
# abstract method decorator for methods 
# Abstract class can contain both abstract and non-abstract methods also
from abc import * 
class Vehicle(ABC): 
    @abstractmethod 
    def noofwheels(self): 
        pass 
class Bus(Vehicle): 
    def noofwheels(self): 
        return 7  
class Auto(Vehicle): 
    def noofwheels(self): 
        return 3 
b=Bus() 
print(b.noofwheels())#7
# BUS should override abstract methods otherwise we get error ( instantation error)