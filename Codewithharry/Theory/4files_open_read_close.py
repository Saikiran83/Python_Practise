#f=open(filename,mode)
#mode=
"""
1)r  open an existing file for read operation. The file pointer is positioned at the 
beginning of the file.If the specified file does not exist then we will get 
FileNotFoundError.This is default mode.
2) w  open an existing file for write operation. If the file already contains some data 
then it will be overridden. If the specified file is not already avaialble then this mode will 
create that file.
3) a  open an existing file for append operation. It won't override existing data.If the 
specified file is not already avaialble then this mode will create a new file.
4) r+  To read and write data into the file. The previous data in the file will not be 
deleted.The file pointer is placed at the beginning of the file.
5) w+  To write and read data. It will override existing data.
6) a+  To append and read data from the file.It wont override existing data.
x  To open a file in exclusive creation mode for write operation. If the file already 
exists then we will get FileExistsError.
Note: All the above modes are applicable for text files. If the above modes suffixed with 
'b' then these represents for binary files.
Eg: rb,wb,ab,r+b,w+b,a+b,xb"""



#1
f=open("5sai.txt") #by default mode is r > read mode only
Content=f.read() ##read the file
print(Content)
f.close()
#2 
f=open("5sai.txt") #by default mode is r > read mode only
Content=f.read(4) ##read the file
print(Content) # read only 4 characters from the text file
f.close()
#3
f=open("5sai.txt") #by default mode is r > read mode only
Content=f.read(5) ##It will read first 5 characters
print(Content)
Content=f.read(5) ##It will read next 5 characters (space also including)
print(Content)
f.close()   
#4
f=open("5sai.txt") #by default mode is r > read mode only
Content=f.read(444) ##read the file whole file
print("1",Content)
Content=f.read() ##read the file
print("2",Content) #just print 2 because nothing left to read
f.close() 
#5
f=open("5sai.txt") #by default mode is r > read mode only
for line in f:
    print(line,end='') ## it will print line by line with new line ch ,so used end
f.close()
#6
f=open("5sai.txt","r")
Content=f.read()
for line in Content:
    print(line) ##it will print character wise 
f.close()
#7
f=open("5sai.txt","r")
print(f.readline()) #print the first line with new line character
print(f.readline())# print the 2nd line 
#8
f=open("5sai.txt","r")
print(f.readlines()) # print the lines in a list