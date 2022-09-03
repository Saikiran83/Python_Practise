# In Python we cannot specify the type explicitly. Based on provided value at 
# runtime the type will be considered automatically. Hence Python is considered as 
# Dynamically Typed Programming Language.
# At runtime if 'it walks like a duck and talks like a duck,it must be duck'. Python follows this 
# principle. This is called Duck Typing Philosophy of Python.

class duck:
    def talk(self):
        print("sound")
class dog:
    def talk(self):
        print("sounds")
def f1(obj):
    obj.talk()
for i in duck(),dog():
    f1(i)
# if talk method is not present then we will get attribute error.
# we need to use hasattr