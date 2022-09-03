# Demo program with variable no of arguements
class Test:
    def sum(self,*a):
        total = 0
        for x in a:
            total = total + x
        print(total)
t = Test()
t.sum(10,20)
t.sum()
t.sum(10)