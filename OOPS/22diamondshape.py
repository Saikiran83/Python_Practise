class A:
    def met(self):
        print("inside class A")
class B(A):
    def met(self):
        print("inside class B")
class C(A):
    def met(self):
        print("inside class C")
class D(B,C):
    def met(self):
        print("inside class D")

d = D()
d.met() 
# output : inside class D
# if nothing is there then in D first we are inheriting B, then it look inside B
# o/p it gives is inside class B otherwise inside class C.
# If not present in both then it look in A, inside class A 
