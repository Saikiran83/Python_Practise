#Input: ABAABBCA
#Output: 4A3B1C
s='ABAABBCA'
output1=''
output2=''
d={}
for ch in s:
    d[ch]=d.get(ch,0)+1
for k,v in sorted(d.items()):
    output1=output1+str(v)+k
    output2=output2+k+str(v)
print(output1)
print(output2)


