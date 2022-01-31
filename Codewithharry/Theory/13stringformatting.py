#1
me="sai"
s="this is %s "%me
print(s)
# for multiple ips
me="sai"
a=3
x="this is %s %s"%(me,a)
print(x)

#using .format
x="this is {} {}".format(me,a)
print(x)
#
x="this is {1} {0}".format(me,a) # take position accordingly
print(x)
import math
#using another f string
x=f"this is {me} {a} {math.cos(60)}"
print(x)