def smart_division(func): 
    def inner(a,b): 
        print("We are dividing",a,"with",b) 
        if b==0: 
            print("OOPS...cannot divide") 
            return 
        else: 
            return func(a,b) 
    return inner 

@smart_division 
def division(a,b): 
    return a/b 
print(division(20,2)) 
print(division(20,0)) 
""" Without Decorator we will get Error. In this Case Output is:
10.0 
Traceback (most recent call last): 
File "test.py", line 16, in <module> 
 print(division(20,0)) 
File "test.py", line 13, in division 
 return a/b 
ZeroDivisionError: division by zero 
With Decorator we won't get any Error. In this Case Output is:
We are dividing 20 with 2
10.0
We are dividing 20 with 0
OOPS...cannot divide
None
 """