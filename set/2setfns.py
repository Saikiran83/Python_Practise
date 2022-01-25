s={10,20,30} 
s.add(40); 
print(s) #{40, 10, 20, 30} 
#update(x,y,z):
#To add multiple items to the set.
 #Arguments are not individual elements and these are Iterable objects like List, Range 
#etc.
 #All elements present in the given Iterable objects will be added to the set.
s={10,20,30} 
l=[40,50,60,10] 
s.update(l,range(5)) 
print(s) 

#s.pop() removes random element from set
# s.remove(x) removes x element from list >we will get error if not present
# s.discard(x) removes specified element> if not present we wont get any error
#.clear() removes all the elements in the set