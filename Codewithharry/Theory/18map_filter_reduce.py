
def func(n):
    return n*n
a=[1,2,3,4,5,6,7,8,9]
s=list(map(func,a))  #map(function,sequence)
print(s)  # maps the values> [1, 4, 9, 16, 25, 36, 49, 64, 81]
######################
def fun(n):
    if n%2 != 0:
        return n
a=[1,2,3,4,5,6,7,8,9]
s1=list(filter(fun,a))  #filter(function,sequence)
print(s1)  # filter the values> [1, 3, 5, 7, 9]

####################
from functools import reduce
a=[1,2,3,4,5,6,7,8,9]
s2=reduce(lambda x,y:x+y,a) #reduce(function,sequence)
print(s2)  # freduce the values to single value > 45