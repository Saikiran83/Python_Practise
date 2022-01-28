def fact_iter(n):
    fact=1
    for i in range(n):
        fact=fact*(i+1)
    return fact
n=int(input("enter number:"))
print(fact_iter(n))

##
def fact_recursive(n):
    if n==1:
        return 1
    else:
        return n*fact_recursive(n-1)
n=int(input("enter number:"))
print(fact_recursive(n))
