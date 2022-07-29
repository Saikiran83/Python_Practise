# when object does not contain any reference variable then object eligible for garbage collection 

##################
import time 
class Test:
    def __init__(self):
        print("constructor called")
    def __del__(self):
        print("destructor called ")
t1=Test() 
t2=t1 
t3=t2 
del t1 
time.sleep(5) 
print("object not yet destroyed after deleting t1") 
del t2 
time.sleep(5) 
print("object not yet destroyed even after deleting t2") 
print("I am trying to delete last reference variable...") 
del t3 