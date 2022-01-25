words="the quick brown fox jumps over the lazy dog".split() 
print(words) 
l=[[w.upper(),len(w)] for w in words] 
print(l) 

v = [2**x for x in range(1,6)] 
print(v) 
m = [x for x in range(10) if x%2==0] 
print(m) 