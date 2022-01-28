"""The with Statement:
 The with statement can be used while opening a file.We can use this to group file 
operation statements within a block.
 The advantage of with statement is it will take care closing of file,after completing all 
operations automatically even in the case of exceptions also, and we are not required 
to close explicitly."""
with open("5sai.txt","w") as f:    
    f.write("Durga\n") 
    f.write("Software\n") 
    f.write("Solutions\n") 
    print("Is File Closed: ",f.closed)   #false
print("Is File Closed: ",f.closed)  #true no need of f.close()