l=[10,20,40,40,20]
l.reverse()   ## reverse the list elements
print(l)

l.sort()
print(l) ## sort the elements 
 ## alphabets ascending order, number also same
 ## to sort the list elements must be homogenerous either str ,int type

l.sort(reverse=True) # sort in reverse order
l.sort(reverse=False) ## by default sort from starting

## Aliasing 
X=list(range(5))
Y=X
## if we change Y , then X also changes 
## to avoid this go for cloning>> copy method
Z=X.copy()
# if we change Z , X won't change

S=X+Y # list concatination
print(S)
A=3*X # repetition of list
## clear function used to clear all the eleemnts of list
print(A.clear())
# nested list
B=[10,20,[10,20],[20,30]]
print(B[2][1])  ## print 30 