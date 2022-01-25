def wish(name,msg): 
    print("Hello",name,msg) 
wish(name="sai",msg="Good Morning")  #keyword arg
wish(msg="Good Morning",name="sai") #keyword
wish("sai","gm")   #positional arguments
#The number of arguments and position of arguments must be matched. If we change 
#the order then result may be changed.
#If we change the number of arguments then we will get error.
#Note: We can use both positional and keyword arguments simultaneously. But first we 
#have to take positional arguments and then keyword arguments,otherwise we will get 
#syntaxerror.
wish("sai","GoodMorning") #Valid 
wish("sai",msg="GoodMorning") # Valid 
#wish(name="sai","GoodMorning") # Invalid ERROR, (positional followed by keyword must)
#3Default Arguments:
#Sometimes we can provide default values for our positional arguments.
def wish(name="Guest"): 
   print("Hello",name,"Good Morning") 
wish("sai") 
wish() #hello guest good morning
#4 VARIABLE LENGTH ARGUMENTS
#def fn(*n) > here we can pass any number of arguments
#internally all these values represented in tuple 
#fn(10), fn(10,20), fn(10,20,30)
#We can mix variable length arguments with positional arguments.
def fn(s,*n):
    sum=0
    for i in n:
        sum=sum+i
    print(sum/s)
fn(10,20,30)
#OR
def fn(s,*n):
    sum=0
    for i in n:
        sum=sum+i
    return(sum/s)
a=fn(10,20,30)
b=fn(10,20,50,100)
print(a)
print(b)

#We can declare key word variable length arguments also.
#For this we have to use **.
#def f1(**n):
# We can call this function by passing any number of keyword arguments. Internally 
#these keyword arguments will be stored inside a dictionary.
def display(**kwargs):
    for k,v in kwargs.items():
        print(k,"=",v) 
display(n1=10,n2=20,n3=30) 
display(rno=100,name="sai",marks=70,subject="Python")