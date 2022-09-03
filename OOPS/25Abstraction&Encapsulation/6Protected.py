# Protected members are accessible within the class and also available to its sub-classes. To define a protected member, prefix the member name with a single underscore _.
# Protected data members are used when you implement inheritance and want to allow data members access to only child classes.
#base class
class Company:
    def __init__(self):
        self._project = 'NLP'
#child class
class Employee(Company):
    def __init__(self,name):
        self.name = name 
        super().__init__()
    def show(self):
        print("Employee name:",self.name)
        #accessed protected members
        print("working on project:",self._project)
c = Employee("Sai")
c.show()

# Direct access protected data member
print('Project:', c._project)