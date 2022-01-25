#union():
#x.union(y)  We can use this function to return all elements present in both sets
#x.union(y) OR x|y.
x = {10, 20, 30, 40} 
y = {30, 40, 50, 60} 
print (x.union(y)) #{10, 20, 30, 40, 50, 60} 
print (x|y) #{10, 20, 30, 40, 50, 60} 
#intersection():
#x.intersection(y) OR x&y.Returns common elements present in both x and y.

print (x.intersection(y)) # {40, 30} 
print(x&y) #{40, 30} 
#difference():
#x.difference(y) OR x-y. Returns the elements present in x but not in y.
print (x.difference(y)) # 10, 20 
print (x-y) #{10, 20} 
print (y-x) #{50, 60} 
#symmetric_difference():
#x.symmetric_difference(y) OR x^y. Returns elements present in either x OR y but not in both.

print (x.symmetric_difference(y)) # {10, 50, 20, 60} 
print(x^y) #{10, 50, 20, 60}

#set comprehension is there
# no slicing and indexing in sets