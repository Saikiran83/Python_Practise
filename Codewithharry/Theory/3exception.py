

x=int(input("enter number 1\n"))
y=int(input("enter number 2\n"))
try:
    z=x/y  
    print(z)
except Exception as e:
    print(e)
    z=None
    print(z)

