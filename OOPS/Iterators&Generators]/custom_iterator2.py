# class Myrange:
#     def __init__(self,start,end):
#         self.start = start
#         self.end = end 
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self.start >= self.end:
#             raise StopIteration
#         current = self.start
#         self.start += 1
#         return current

# num = Myrange(1,6)
# for i in num:
#     print(i)

def Myrange(start,end):
    current = start 
    while current < end :
        yield current
        current += 1
m = Myrange(1,6)
for i in m:
    print(i)
