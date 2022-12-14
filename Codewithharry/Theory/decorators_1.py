""" Decorator is a function which can take a function as argument and extend its functionality 
and returns modified function with extended functionality.
 
The main objective of decorator functions is we can extend the functionality of existing 
functions without modifies that function. """

def wish(name): 
    print("Hello",name,"Good Morning") 

""" This function can always print same output for any name
Hello Durga Good Morning
Hello Ravi Good Morning
Hello Sunny Good Morning
But we want to modify this function to provide different message if name is Sunny.
We can do this without touching wish() function by using decorator. """

def decor(func): 
    def inner(name): 
        if name=="Sunny": 
            print("Hello Sunny Bad Morning") 
        else: 
            func(name) 
    return inner 

@decor 
def wish(name): 
    print("Hello",name,"Good Morning") 
# wish("Durga") = decor(durga)
wish("Durga") 
wish("Ravi") 
wish("Sunny") 
