# How we can handle Overloaded Method Requirements in Python:
# Most of the times, if method with variable number of arguments required then we can 
# handle with default arguments or with variable number of argument methods.

# Demo Program with Default Arguments 
class Test: 
    def sum(self,a=None,b=None,c=None): 
        if a!=None and b!= None and c!= None: 
            print('The Sum of 3 Numbers:',a+b+c) 
        elif a!=None and b!= None: 
            print('The Sum of 2 Numbers:',a+b) 
        else: 
            print('Please provide 2 or 3 arguments') 
t=Test() 
t.sum(10,20) 
t.sum(10,20,30) 
t.sum(10) 