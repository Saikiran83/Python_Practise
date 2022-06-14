from functools import partial
from this import d
def multiply(x,y):
    return x*y
multiply_3 = partial(multiply,3) # stores 3 as one arguement  
print(multiply_3(6))