#raise is used to define user exceptions other than predefined exceptions
class TooYoungException(Exception):
    def __init__(self,arg):
        self.msg=arg 
class TooOldException(Exception): 
    def __init__(self,arg): 
        self.msg=arg 
 
age=int(input("Enter Age:")) 
if age>60: 
    raise TooYoungException("Plz wait some more time you will get best match soon!!!")
elif age<18: 
    raise TooOldException("Your age already crossed marriage age...no chance of getting marriage") 
else: 
    print("You will get match details soon by email!!!") 
