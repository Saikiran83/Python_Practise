l=eval(input("enter list:"))
n=int(input("enter no to search for 2nd occurence:"))
x=l.index(n)
y=l.index(n,x+1,len(l))
l.pop(y)
print("updated list:",l)