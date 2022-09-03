# Demo Program with hasattr() Function:
class Duck: 
    def talk(self): 
        print('Quack.. Quack..') 
class Human: 
    def talk(self): 
        print('Hello Hi...')  
class Dog: 
    def bark(self): 
        print('Bow Bow..')  
def f1(obj): 
    if hasattr(obj,'talk'): 
        obj.talk() 
    elif hasattr(obj,'bark'): 
        obj.bark()
for i in Duck(), Human(), Dog():
    f1(i)