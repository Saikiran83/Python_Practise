class employee:
    no_of_leaves=10
    pass

sai = employee()
kiran = employee()

sai.name = "saikiran"
sai.age = '24'
kiran.name = "kiran"  # instance variables
kiran.age = "24"
print(sai.name)
print(sai.__dict__)
sai.no_of_leaves = 10 # only this object attributes changes 
print(sai.__dict__)  
print(employee.__dict__)
employee.no_of_leaves = 11  
print(employee.__dict__)
