# Demo Program for Deserialization from json String

import json 
json_string='''{
 "name": "durga",
 "age": 35,
 "salary": 1000.0,
 "ismarried": true,
 "ishavinggirlfriend": null
 }''' 
emp_dict=json.loads(json_string) 
print(type(emp_dict)) 
print('Employee Name:',emp_dict['name']) 
print('Employee Age:',emp_dict['age']) 
print('Employee Salary:',emp_dict['salary']) 
print('Is Employee Married:',emp_dict['ismarried']) 
print('Is Employee Has GF:',emp_dict['ishavinggirlfriend'])  
for k,v in emp_dict.items(): 
    print('{} : {}'.format(k,v)) 