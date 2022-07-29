import sys 
class Test: 
   pass 
t1=Test() 
t2=t1 
t3=t1 
t4=t1 
print(sys.getrefcount(t1)) 

# NOTE : for every object, python internally maitains one reference varible self