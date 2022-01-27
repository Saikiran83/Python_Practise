f=open("sai2.txt",'w') 
list=["sunny\n","bunny\n","vinny\n","chinny"] 
f.writelines(list) 
print("List of lines written to the file successfully") 
f.close() 
#output:
#sunny
#bunny
#vinny
#chinny
#Note: While writing data by using write() methods, compulsory we have to provide line 
#seperator(\n), otherwise total data should be written to a single line
f=open("sai2.txt","w")  #if file is there it write the below line 
                        #otherwise it creates the new file
#f.write("hai Sai,get out of comfort zone")
f.write("hello")
f.close()
# if we run write again it will take the text which we give in the write
#by removing the old textfile data

#to add to the text data > we need to use append method
f=open("sai2.txt","a")
f.write("you need to push harder")
f.close()

#to read and write
f=open("sai2.txt","r+")
f.read()
f.write("hey u")
f.close()

