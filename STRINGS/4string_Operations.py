#@replce method(Here new object created,we can't change the original>str is immutable)
#s.replace(oldstring, newstring)
s='saikiran need to put extra effort'
s1=s.replace('saikiran','sai')
print(s1)

#we can split the given string according to specified seperator by using @split() method.
# #l = s.split(seperator)
#The default seperator is space. The return type of split() method is List.
s="22-02-2018" 
l=s.split('-')  ##defult is space ' '
for x in l: 
   print(x)

#joining of Strings:
#We can join a Group of Strings (List OR Tuple) wrt the given Seperator.
#s = seperator.join(group of strings)
t = ('sunny', 'bunny', 'chinny')
s = '-'.join(t)
print(s)