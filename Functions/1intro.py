#def function_name(parameters) :
 ##""" doc string"""
 #----
 #-----
 #return value
#Note: While creating functions we can use 2 keywords
#def (mandatory)
#return (optional)
def fact(num): 
   result=1 
   while num>=1: 
       result=result*num 
       num=num-1 
   return result 
for i in range(1,5): 
    print("The Factorial of",i,"is :",fact(i))

#return multiple values from a fn
def sum_sub(a,b):
    sum=a+b
    sub=a-b
    return sum,sub
x,y=sum_sub(100,50)
print("the sum is",x)
print("the sub is",y)
#another method for print
z=sum_sub(20,30)
for i in z:
    print(i)