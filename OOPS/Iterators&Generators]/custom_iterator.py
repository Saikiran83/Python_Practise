class PowerTwo:
    # Class to implement an iterator of powers of two
    # Constructor accepting the max value
    def __init__(self,max=0):
        self.max = max
    # defined __iter__() to point the first element
    def __iter__(self):
        self.n = 1
        return self
   # __next__() to fetch the next value from the iterator
    def __next__(self):
        if self.n <= self.max:
            result = 2 ** self.n
            self.n += 1 
            return result 
        # Terminating condition
        else:
            raise StopIteration
# create an object
numbers = PowerTwo(4)
# create an iterable from the object
i = iter(numbers)
# Using for-in loop to print the elements up to max
for it in i:
   print(it)

# # Program to print the Power of two up to the given number using generator
# def PowerTwoGen( max=0 ):
#    n = 1
#    while n < max:
#        yield 2 ** n
#        n += 1

# a = PowerTwoGen(6)

# # Printing the values stored in a
# for i in a:
#    print(i)