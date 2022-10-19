import json 
employee={'name':'durga', 
 'age':35, 
 'salary':1000.0, 
 'ismarried':True, 
 'ishavinggirlfriend':None 
 } 
json_string = json.dumps(employee,indent=4,sort_keys=True) 
print(json_string) 
with open('emp.json','w') as f:  
    json.dump(employee,f,indent=4)