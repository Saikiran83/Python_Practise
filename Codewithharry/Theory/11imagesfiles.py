#Program to read Image File and write to a New Image File?
f1=open("rossum.jpg","rb")  #read
f2=open("newpic.jpg","wb") #write
bytes=f1.read() 
f2.write(bytes) 
print("New Image is available with the name: newpic.jpg")