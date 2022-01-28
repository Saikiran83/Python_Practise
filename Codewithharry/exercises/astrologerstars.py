#right angle triangle 
n=int(input("number of lines:"))
n2=int(input("print 1 | 0 for execution:"))
if bool(n2)==True:
    for i in range(1,n):
        print(""*(n-i)+" *"*i)
if bool(n2)==False: #reverse
    for i in range(1,n):
        print(""*(i)+" *"*(n-i))
   
##diamond print
n=int(input("number of lines:"))
n2=int(input("print 1 | 0 for execution:"))
if bool(n2)==True:
    for i in range(1,n):
        print(" "*(n-i)+" *"*i)
if bool(n2)==False:#reverse
    for i in range(1,n):
        print(" "*(i)+" *"*(n-i))
   

 

