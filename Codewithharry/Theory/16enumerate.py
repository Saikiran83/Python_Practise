l=["apple","banana","orange","sapota","cream"]
i=0
for item in l:
    if i%2!=0:
        print(f"hey sai buy {item}")
    i=i+1

############ USING ENUMERATE
for index,item in enumerate(l):
    if index%2 is not 0:
        print(f"hey sri dont buy {item}")
##########################

l1 = ["eat","sleep","repeat"]

# printing the tuples in object directly
for ele in enumerate(l1):
	print (ele)

# changing index and printing separately
for count,ele in enumerate(l1,100):  ##enumerate(iterable,index) default is 0
	print (count,ele)

#getting desired output from tuple
for count,ele in enumerate(l1):
    print(count)
    print(ele)
