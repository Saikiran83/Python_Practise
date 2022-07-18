#*instance variables changes from object to object
#once we create a object copy of instance variables are created 

class employee:
    def __init__(self,name,age):
        self.name = name
        self.age = age 
    def sai(self):
        print("the age of kiran is {}".format(self.age))
s = employee('sai',25)
s.sai()

#####################

#static varibales 

#variables which are constant for all the objects 
#for class, only one set of static varibles created 

class sai:
    x = 10
    def sai(self):
        print("hi",sai.x)
s1 = sai()
s1.sai()

#####
# local variables : varibales which are created inside methods for temperory requirements 

