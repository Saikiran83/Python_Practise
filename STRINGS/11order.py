#input: a4k3b2
#Output: aeknbd
#In this example the following two functions are required to use
#ord(): To find unicode value for the given character
 #Eg: print(ord('a')) #97
#chr(): To find corresponding character for the given unicode value
 #Eg: print(chr(97)) # a
s='a4k3b2'
output=''
for ch in s:    
    if ch.isalpha():
         x=ch
         output=output+ch
    else:
         d=int(ch)
         newc= chr(ord(x)+d)
         output=output+newc
print(output)