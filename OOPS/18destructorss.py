# The destructor was called after the program ended or when all the references to object are deleted i.e when the reference count becomes zero, not when object went out of scope.

# Python program to illustrate destructor

class Employee:
	# Initializing
	def __init__(self):
		print('Employee created')
	# Calling destructor
	def __del__(self):
		print("Destructor called")
def Create_obj():
	print('Making Object...')
	obj = Employee()
	print('function end...')
	return obj

print('Calling Create_obj() function...')
obj = Create_obj()
print('Program End...')


