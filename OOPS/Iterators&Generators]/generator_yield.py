def square_numbers(num):
    result = []
    for i in num:
        result.append(i*i)
    return result
my_nums = square_numbers([1,2,3,4])
print(my_nums)

# generator function 
def square_numbers(num):
    for i in num:
        yield i*i

my_num = square_numbers([1,2,3])
for i in my_num:
    print(i)

## generator comprehension ( we use () brackets for list comprehension we use [])
mynum = (x*x for x in [1,2,3])
print(mynum)
print(list(mynum))

#########################

import random

def lottery():
    # returns 6 numbers between 1 and 40
    for i in range(6):
        yield random.randint(1, 40)

    # returns a 7th number between 1 and 15
    yield random.randint(1, 15)

for random_number in lottery():
       print("And the next number is... %d!" %(random_number))