# To print given number of *s in a row



n=int(input("enter a number:"))
for i in range(n):
    print("*",end='') #defult for end is new line character,it specifies string chracter to end 

#: To printsquare pattern with * symbols
for i in range(n):
    print("*"*n)

#To print square pattern with provided fixed digit in every row
for i in range(n):
    print((str(i+1)+' ')*n)

#To print square pattern with alphabet symbols
for i in range(n):     
    print((chr(65+i)+' ')*n) 
#

