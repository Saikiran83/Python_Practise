# destructor is a special method in python & name should be __del__
# garbage collector destroy the object, before that it calls the destructor to perform clean up activities 
# NOTE: the job of DESTRUCTOR is not to destroy the object and it is just to perform clean up activities  
import time 
class Test: 
    def __init__(self): 
        print("Object Initialization...") 
    def __del__(self): 
        print("Fulfilling Last Wish and performing clean up activities...")  
t1=Test() 
t1=None 
time.sleep(5) # after 5 secs it will be cleaned 
print("End of application") 

###############
# Python program to illustrate destructor
class Employee:

	# Initializing
	def __init__(self):
		print('Employee created.')

	# Deleting (Calling destructor)
	def __del__(self):
		print('Destructor called, Employee deleted.')

obj = Employee()
del obj ## automatically calls the destructor 


