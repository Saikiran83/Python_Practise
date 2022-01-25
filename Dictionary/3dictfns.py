#d={}
#d[key]=value > to update the dict, if value present then old value replaced with new value
#>if not ,new value will be created

#d.clear() >clear the contents of the dict
#del d[key] > remove the specific key
# del d >delete the total dict
#d.get(key,default)> if key available returns the value otherwise default value
#d.keys() > returns the keys
#d.values() > returns the values
#d.items()> returns tuple of key value pairs
d={100:"durga",200:"ravi",300:"shiva"} 
for k,v in d.items(): 
    print(k,"--",v)   
#Output
#100 -- durga 
#200 -- ravi 
#300 -- shiva 
#d.setdefault(k,v) > if key available it returns the corresponding value, otherwise adds to dict

#dict comprehension
squares={x:x*x for x in range(1,6)} 
print(squares) 
doubles={x:2*x for x in range(1,6)} 
print(doubles) 
