class InfiniteIterator:
 
    def __iter__(self):
        self.n = 0
        return self
 
    def __next__(self):
        result = self.n * 2
        self.n += 1
        return result
 
multiplesOfTwo = InfiniteIterator()
 
i = iter(multiplesOfTwo)
 
print("Multiples of two are:")
print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(next(i))

# it will keep on continue , because there is no max value to raise exception here