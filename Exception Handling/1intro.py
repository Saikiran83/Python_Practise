x=int(input("enter number 1\n"))
y=int(input("enter number 2\n"))
try:
    z=x/y  
    print(z)
except Exception as e:
    print(e)
    z=None
    print(z)

#try with multiple exceptions
try: 
   x=int(input("Enter First Number: ")) 
   y=int(input("Enter Second Number: ")) 
   print(x/y) 
except ZeroDivisionError : #except Exception as e ,if we dont know the error.
   print("Can't Divide with Zero") 
except ValueError: 
   print("please provide int value only")
