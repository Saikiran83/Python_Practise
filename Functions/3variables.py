#global variables> we declare outside fn & can access everywhere
#local variables>declare inside fn > access only inside that fn where we declared
a=10 # global variable 
def f1(): 
   print(a)  #10
def f2(): 
   print(a)  #10

def f1(): 
   a=10 
   print(a) # valid 10
def f2(): 
   print(a) #invalid
   #using global keyword
def f1(): 
   global a 
   a=10 
print(a) 
 
def f2(): 
   print(a)  
f1() 
f2()
#Note: If global variable and local variable having the same name then we can access 
#global variable inside a function as follows
a = 10 #Global Variable 
def f1(): 
    a=777 #Local Variable 
    print(a) 
    print(globals()['a']) 
f1()  #output will be 777,10