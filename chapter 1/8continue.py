#skip the current iteration and continue the next iteration
cart=[100,200,50,500,700,10]
for item in cart:
    if item>=500:
        print("we cannot process this item:",item)
    print(item)