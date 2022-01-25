#tuple is same as list except tuple is immutable
t=(10,) # must include , otherwise it takes as int
x=(10)
print(type(t))
print(type(x))

#we can create by using tuple function also
#slicing, indexing also there
# immutable
t = (40,10,30,20) 
print(min(t)) # 10 
print(max(t)) #40

a = 10
b = 20
c = 30
d = 40
t = a, b, c, d
print(t) #(10, 20, 30, 40)
#Here a, b, c, d are packed into a Tuple t. This is nothing but Tuple packing.
#Tuple unpacking is the reverse process of Tuple packing.
#We can unpack a Tuple and assign its values to different variables.
t=(10,20,30,40) 
a,b,c,d=t 
print("a=",a,"b=",b,"c=",c,"d=",d)

###Tuple comprehension is not supported by python