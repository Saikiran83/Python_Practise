class student:
    legs = 2
    @classmethod
    def walk(cls,name):
        print("{} walks with {} legs".format(name,cls.legs))
print(student.walk('sai'))  # output will be sai walks with 2 legs and None
# None will be default if we print class method
student.walk('sai') # here output will be sai walks with 2 legs only

#Program to track the Number of Objects created for a Class:
class Test: 
    count=0 
    def __init__(self): 
        Test.count =Test.count+1 
    @classmethod 
    def noOfObjects(cls): 
        print('The number of objects created for test class:',cls.count) 
 
t1=Test() 
t2=Test() 
Test.noOfObjects()  ## init called twice so 2
t3=Test() 
t4=Test() 
t5=Test() 
Test.noOfObjects() # till here it is called 5 times 