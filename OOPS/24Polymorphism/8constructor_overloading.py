# Constructor Overloading:
# Constructor overloading is not possible in Python.
# If we define multiple constructors then the last constructor will be considered.
class Test: 
    def __init__(self): 
        print('No-Arg Constructor')  
    def __init__(self,a): 
        print('One-Arg constructor')  
    def __init__(self,a,b): 
        print('Two-Arg constructor') 
#t1=Test() 
#t1=Test(10) 
t1=Test(10,20) 
# Output: Two-Arg constructor
# In the above program only Two-Arg Constructor is available.
# But based on our requirement we can declare constructor with default arguments and 
# variable number of arguments