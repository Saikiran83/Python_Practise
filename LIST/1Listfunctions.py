#LIST function
s=list(range(0,20,4))
print(s)

#split function
x="saikiran needs to put extra effort"
l=x.split()  ##gives values in list
print(l) 
# slice operator
#s[start:stop:step]
L=[1,2,3,2,3,2,3,4,55,56,5,5,6,6,7]
print(len(L))##returns number of elements present inside the list

print(L.count(1)) ## returns the count of 1 in list

print(L.index(2)) ## returns the index of first occurence in list

L.append(100) ## add 100 at last index
print(L)

L.insert(25,3) #insert 25 at index 3
print(L)

##extend add one list to another list
## list1.extend(list2)

L.remove(2) # remove first occurence if multiple times it exist
print(L)

# L.pop() > remove last element of list 
# L.pop(index) > remove element present at specific index

