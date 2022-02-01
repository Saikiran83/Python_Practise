import time
intial=time.time()
k=0
while k<=5:
    print("sai, push hard day by day")
    k+=1
print("while loop run in",time.time()-intial,"seconds")
intial2=time.time()
for i in range(5):
    print("sai, push hard day by day ")
print("for loop runs in",time.time()-intial2,"second") 
