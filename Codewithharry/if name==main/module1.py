################
def func(string):
    return f"hello {string} how r u"
def add(a,b):
    return a+b+10
print("the name is",__name__)   # here it will return main (means main function)
if __name__== '__main__':
    print(func("sai"))
    c=add(10,15)
    print(c)
