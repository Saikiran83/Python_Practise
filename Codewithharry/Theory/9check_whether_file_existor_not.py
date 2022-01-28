#Write a Program to check whether the given File exists OR not. If it is 
 #available then print its content?
import os,sys 
fname=input("Enter File Name: ") 
if os.path.isfile(fname): 
    print("File exists:",fname) 
    f=open(fname,"r") 
else: 
    print("File does not exist:",fname) 
    sys.exit(0) 
print("The content of file is:") 
data=f.read() 
print(data) 

#Note:
#sys.exit(0) To exit system without executing rest of the program.
#argument represents status code. 0 means normal termination and it is the default value