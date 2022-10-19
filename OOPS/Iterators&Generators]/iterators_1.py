# There are some objects which are iterable, which means we can traverse over them and they will return their member value one by one.

# Examples of iterable objects are: List, Tuple, Dictionary
# Iterators in python also objects, they are used for iterating iterables
# we can use iterators on lists, tuples, dictionaries, and strings.
# Iterators can use methods such as iter(), next()


mySecret = ["I", "Love", "Python"]
myIter = iter(mySecret)
print(myIter)
 
# print(next(myIter))
# print(next(myIter))
# print(next(myIter)) # if we print next again we will get error because no value 
while True:
    try:
        print(next(myIter))
    except StopIteration:
        break