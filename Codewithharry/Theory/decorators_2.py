def dec(func):
    def inner(a,b):
        print("###@#@##")
        print("the sum is:", end='')
        func(a,b)
        print("#@####@#@")
    return inner
@dec
def add(a,b):
    print(a+b)

add(20,30)

#How to call Same Function with Decorator and without Decorator:
#We should not use @decor

def decor(func): 
    def inner(name): 
        if name=="Sunny": 
            print("Hello Sunny Bad Morning") 
        else: 
            func(name) 
    return inner 
def wish(name): 
    print("Hello",name,"Good Morning") 
 
decorfunction = decor(wish) 
wish("Durga") #decorator wont be executed 
wish("Sunny") #decorator wont be executed 
 
decorfunction("Durga")#decorator will be executed 
decorfunction("Sunny")#decorator will be executed