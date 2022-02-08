
def wish(name):
    print("good morning:",name)
    
greet = wish   # wish , greet are of same ids 
wish("sai")  # if we delete wish also we can get output when we run greet 
greet("sai")  

###############################
def outer():
    print("outer fn started")
    def inner():
        print("inner fn started")
    inner()   # if we dont call this function here(print("inner fn started") won't execute)
    print("outer fn executed")
outer()
#inner() , if we call here we get error because inner is local to outer fn