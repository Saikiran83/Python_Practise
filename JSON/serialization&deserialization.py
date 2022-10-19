# How to perform serialization and deserialization of 
# customized class objects:
# json.dumps()  python dict to json string
# json.dump()  python dict to json file
# dump(),dumps() functions will work only for python dict objects, and we cannot use for 
# our customized class objects like Employee, Customer etc.
# json.loads()  json string to python dict
# json.load()  json file to python dict
# load() and loads() functions will always provide python dict objects as return type and we 
# won't get our customized class objects directly.
# The required conversions we have to take care explicitly.

import json 
class Employee: 
    def __init__(self,eno,ename,esal,eaddr): 
        self.eno=eno 
        self.ename=ename 
        self.esal=esal 
        self.eaddr=eaddr 
    def display(self): 
        print('ENO:{}, ENAME:{}, ESAL:{}, EADDR:{}'.format(self.eno,self.ename,self.esal,self.eaddr))  
e=Employee(100,'Durga',1000.0,'Hyderabad')  
#emp_dict={'eno':e.eno,'ename':e.ename,'esal':e.esal,'eaddr':e.eaddr}  
emp_dict=e.__dict__  
with open('emp.json','w') as f: 
    json.dump(emp_dict,f,indent=4) 
with open('emp.json','r') as f: 
    edict = json.load(f) 
#print(type(edict)) 
 
newE=Employee(edict['eno'],edict['ename'],edict['esal'],edict['eaddr']) 
 
newE.display()