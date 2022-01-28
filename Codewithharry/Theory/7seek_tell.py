f=open("sai2.txt")
print(f.tell()) # tell where our pointer is
print(f.readline()) 
print(f.tell()) # tell where our pointer is after first reading first line
print(f.readline())
f.close()

## seek()
f=open("sai2.txt")
print(f.readline()) 
print(f.seek(4))# it tells pointer to start at 4 th position for next line read
print(f.readline())
f.close()
