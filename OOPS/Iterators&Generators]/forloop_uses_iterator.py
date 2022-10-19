num = range(5)
for i in num:
    print(i)

# Behind the scenes :

# num = range(5)
# num_iter_obj = iter(num)
# while True:
#     try:
#         print(next(num_iter_obj))
#     except StopIteration:
#         break