""" For num() function we are applying 2 decorator functions. First inner decorator will work 
and then outer decorator. """

def decor1(func): 
    def inner(): 
        x=func() 
        return x*x 
    return inner 
def decor(func): 
    def inner(): 
        x=func() 
        return 2*x 
    return inner 

@decor1 
@decor 
def num(): 
    return 10 
 
print(num())  # 400 output 
# here first inner decorator which is decor , next decor1 
# 20 >  20*20 = 400