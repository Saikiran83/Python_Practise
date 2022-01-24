from itertools import count


s='ABCDABXXXBCDABBBBCCCZZZZCDDDDEEEEEF'
l=[]
for ch in s:
    if ch not in l:
        l.append(ch)
for ch in sorted(l):    
    print('{} occurrs {} times'.format(ch,s.count(ch)))
###without count method
print("2nd method")
d={}
for ch in s:
    d[ch]=d.get(ch,0)+1
for k,v in d.items():
    print('{} occurrs {} times'.format(k,v))