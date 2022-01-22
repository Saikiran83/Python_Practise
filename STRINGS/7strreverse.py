#1st method
s = input('Enter Some String to Reverse:')
output = s[::-1]
print("first method:",output)

#2nd method
r=reversed(s)
output=''.join(r)
print("2nd method:",output)

#3rd method

output=''
i=len(s)-1
while i>=0:
   output=output+s[i]
   i=i-1
print("3rd method:",output)
