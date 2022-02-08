
def outer():
    def inner():
        print("inner fn executed")
    return inner
f = outer()
f()    

# f = outer > here we r alliasing outer to f, both these objects call the same fn 
f1 = outer # it wont execute >  
f1() # it wont execute > it will execute only when we call inner function inside in place of return
""" 
def outer():
    def inner():
        print("inner fn executed")
    inner()
f = outer  # this is aliasing execute only when we call inner inside
f() """  # here it will print the statement

""" f = outer > both pointing to same object
f = outer() > outer fn executed and that return value is stored in f 
             whenever we call f that inner fn gets executed and gives return """