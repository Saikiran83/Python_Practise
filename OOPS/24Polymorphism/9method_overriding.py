# What ever members available in the parent class are bydefault available to the child 
# class through inheritance. If the child class not satisfied with parent class 
# implementation then child class is allowed to redefine that method in the child class 
# based on its requirement. This concept is called overriding.
# ⚽ Overriding concept applicable for both methods and constructors.

# method overriding using super
class P: 
    def property(self): 
        print('Gold+Land+Cash+Power') 
    def marry(self): 
        print('Appalamma') 
class C(P): 
    def marry(self): 
        super().marry() 
        print('Katrina Kaif')
c = C()
c.marry()

# From Overriding method of child class,we can call parent class method also by using 
# super() method.
