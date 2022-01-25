#recursive fn
from ast import Expression


def factorial(n):
    if n==0:
        result=1
    else:
        result=n*factorial(n-1)
    return result
for i in range(5):
    print("the factorial of ",i,"is",factorial(i)) 
#lambda function
#lambda aurgument_list:Expression 
s=lambda x: x*x 
print("the square of 2 is",s(2))
s=lambda a,b:a+b 
print("The Sum of 10,20 is:",s(10,20)) 
print("The Sum of 100,200 is:",s(100,200))
#filter() Function:
#We can use filter() function to filter values from the given sequence based on some condition.
#filter(function,sequence)
l=[0,5,10,15,20,25,30] 
l1=list(filter(lambda x:x%2==0,l)) 
print(l1) #[0,10,20,30] 

#map() function
#for every element present in the given sequence,apply some functionality and 
#generate new element with the required modification.
#map(function, sequence)
l=[1,2,3,4,5] 
l1=list(map(lambda x:2*x,l)) 
print(l1) #[2, 4, 6, 8, 10] 

#reduce() Function:
# reduce() function reduces sequence of elements into a single element by applying the 
#specified function.
#reduce(function,sequence)
#reduce() function present in functools module and hence we should write import statement.
from functools import * 
l=[10,20,30,40,50] 
result=reduce(lambda x,y:x+y,l) 
print(result) # 150
