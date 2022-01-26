#We can use default except block to handle any type of exceptions.
#In default except block generally we can print normal error messages.
#Syntax: 
 #except:
 #   statements
try:
    x=int(input("Enter First Number: ")) 
    y=int(input("Enter Second Number: ")) 
    print(x/y) 
except ZeroDivisionError: 
    print("ZeroDivisionError:Can't divide with zero") 
except: 
    print("Default Except:Plz provide valid input only") 

###Note: If try with multiple except blocks available then default except block should be 
 #last, otherwise we will get SyntaxError.
try:    
    print(10/0) 
except:
    print("Default Except") 
except ZeroDivisionError:     
    print("ZeroDivisionError") 
#SyntaxError: default 'except:' must be last    ####