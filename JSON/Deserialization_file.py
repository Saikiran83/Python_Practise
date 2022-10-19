# Demo Program for Deserialization from json file

import json
with open('emp.json','r') as f:
    emp_dict = json.load(f)
print(type(emp_dict)) 
print('Employee Name:',emp_dict['name']) 
print('Employee Age:',emp_dict['age']) 
print('Employee Salary:',emp_dict['salary']) 
print('Is Employee Married:',emp_dict['ismarried']) 
print('Is Employee Has GF:',emp_dict['ishavinggirlfriend'])  
for k,v in emp_dict.items(): 
    print('{} : {}'.format(k,v))