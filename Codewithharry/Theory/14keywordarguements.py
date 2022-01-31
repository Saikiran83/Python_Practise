def funcargs(*args):
    print(type(args))
    print(args[0])
names=["sai","kiran",'T'] # always takes as tuple onlys
funcargs(*names) # we take all arguments at a time
###
def funcargs(*args):    
    for item in args:
        print(item)
names=["sai","kiran",'T'] 
funcargs(*names)
####
def func(normal,*args):
    print(normal)
    for item in args:
        print(item)
normal="this is normla"
names=["sai","kiran"]
func(normal,*names) # if we take *args first then we will get error, default argument always first

##############
def funck(normal,*args,**kwargs):
    print(normal)
    for item in args:
        print(item)
    for k,v in kwargs.items():
        print(f"{k} has {v}")
normal="hi hello"
name=("sai","kiran")
dicts={"sai":23,"kiran":24}
funck(normal,*name,**dicts)