# W/O Existing container object there is no space for contained object --> strongly associated
# called compostion
# Ex: w/o existence of university there is no existence of department 
# W/O existing container object there is a chance for contained object existence --> weakly associated
# called aggregation
# Ex: w/o existence of department there is a chance for existence of professor 

class student:
    college_name = 'SAIKIRAN'
    def __init__(self,name):
        self.name = name
print(student.college_name)
s = student('SAI')
print(s.name)