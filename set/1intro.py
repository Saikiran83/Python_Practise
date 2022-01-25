#If we want to represent a group of unique values as a single entity then we should go 
#for set.
#Duplicates are not allowed.
#Insertion order is not preserved.But we can sort the elements.
#Indexing and slicing not allowed for the set.
#Heterogeneous elements are allowed.
#Set objects are mutable i.e once we creates set object we can perform any changes in 
#what object based on our requirement.
s={10,20,30,40} 
print(s) 
print(type(s)) 
l = [10,20,30,40,10,20,10] 
s=set(l) 
print(s) # set fn
s={} # empty space by default dict