#input: B4A1D3
#output: ABD134
s='B4A1D3'
alphabets=[]
digits=[]
for ch in s:
    if ch.isalpha():
        alphabets.append(ch)
    else:
        digits.append(ch)
output=''.join(sorted(alphabets)+sorted(digits))
print(output)

#A3B4C2
#AAABBBBCC
s='A3C4B2'
output=''
for ch in s:
    if ch.isalpha():
        x=ch
    else:
        d=int(ch)
        output=output+x*d
print(''.join(sorted(output)))##gives sorted op AAABBCCCC
print(output)#AAACCCCBB
