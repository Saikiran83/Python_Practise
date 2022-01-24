#Input: AZZZBCDABBCDABBBBCCCCDDDDEEEEEF
#Output: AZBCDEF
output=''
s='AZZZBCDABBCDABBBBCCCCDDDDEEEEEF'
#1st method
for ch in s:
    if ch not in output:
        output=output+ch
print("1st method",output)

#2nd method
l=[]
for ch in s:
    if ch not in l:
        l.append(ch)
print("2nd method",''.join(sorted(l)))

#3rd method
print(''.join(set(s)))