#Except with multiple exceptions
try:
    x=int(input("Enter First Number: ")) 
    y=int(input("Enter Second Number: ")) 
    print(x/y) 
except (ZeroDivisionError,ValueError) as msg:
    print("Plz Provide valid numbers only and problem is: ",msg)