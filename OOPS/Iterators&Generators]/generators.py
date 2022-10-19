# Generators in Python are used to create iterators and return a traversal object. It helps in traversing all the items one at a time with the help of the keyword yield.\
# Python's generator functions are used to create iterators(which can be traversed like list, tuple) and return a traversal object. It helps to transverse all the items one at a time present in the iterator.
# Generator function used yield key word, whereas normal function uses return keyword

# yied : It is responsible for controlling the flow of the generator function. After returning the value from yield, it pauses the execution by saving the states.
# return : Return statement returns the value and terminates the function.
    #   ***** 
# Difference Between Generator Function & Normal Function
# In generator functions, there are one or more yield functions, whereas, in Normal functions, there is only one function
# When the generator function is called, the normal function pauses its execution, and the call is transferred to the generator function.
# Local variables and their states are remembered between successive calls.
# When the generator function is terminated, StopIteration is called automatically on further calls.

#  ****  USE OF GENERATORS ********  #




# 1 Easy to implement
# Generator functions are easy to implement as compared with iterators. In iterators, we have to implement iter(), __next__() function to make our iterator work.
# 2. Memory Efficient:
# Generator Functions are memory efficient, as they save a lot of memory while using generators. A normal function will return a sequence of items, but before giving the result, it creates a sequence in memory and then gives us the result, whereas the generator function produces one output at a time.

# 3. Infinite Sequence:
# We all are familiar that we can't store infinite sequences in a given memory. This is where generators come into the picture. As generators can only produce one item at a time, so they can present an infinite stream of data/sequence.



