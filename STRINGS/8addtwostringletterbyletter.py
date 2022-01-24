#1 THIS WITH STRINGS WITH DIFF LENGHT
x=input("enter a string:")
y=input("enter another:")
output=''
i,j=0,0
while i<len(x) or j<len(y):
    if i<len(x):
        output=output+x[i]
        i+=1
    if j<len(y):
        output=output+y[j]
        j=j+1
print(output)
#FOR STRING WITH SAME LENGTH\
output=list(map(lambda a,b:a+b,x,y))
print(''.join(output))
#for string with same length
s1='RAVI'
s2='TEJA'
output=''
i,j=0,0
while i<len(s1) or j<len(s2):
    output=output+s1[i]+s2[j]
    i=i+1
    j=j+1
print(output)