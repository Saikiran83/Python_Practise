# we can use same operator for multiple purposes --> operator overloading
# python supports operator overloading
# Demo program to use + operator for class objects ----

class book:
    def __init__(self,books):
        self.books = books
    def __add__(self,other):  # if we dont use this then we get error 
        return self.books + other.books
s1 = book(100)
s2 = book(200)
print(s1+s2) 

# For every operator Magic Methods are available. To overload any operator we have to 
# override that Method in our class. 
# Internally + operator is implemented by using __add__() method.This method is called 
# magic method for + operator. We have to override this method in our class.

# The following is the list of operators and corresponding magic methods.
# 1) +      object.__add__(self,other)
# 2) -      object.__sub__(self,other)
# 3) *      object.__mul__(self,other)
# 4) /      object.__div__(self,other)
# 5) //     object.__floordiv__(self,other)
# 6) %      object.__mod__(self,other)
# 7) **     object.__pow__(self,other)
# 8) +=     object.__iadd__(self,other)
# 9) -=     object.__isub__(self,other)
# 10) *=    object.__imul__(self,other)
# 11) /=    object.__idiv__(self,other) 
# 12) //=   object.__ifloordiv__(self,other)
# 13) %=    object.__imod__(self,other)
# 14) **=   object.__ipow__(self,other)
# 15) <     object.__lt__(self,other)
# 16) <=    object.__le__(self,other)
# 17) >     object.__gt__(self,other)
# 18) >=    object.__ge__(self,other)
# 19) ==    object.__eq__(self,other)
# 20) !=    object.__ne__(self,other)






