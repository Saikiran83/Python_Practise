n=int(input("enter the number to guess:"))
print("maximum number of guesses is 9")
number_of_guesses=1
while number_of_guesses<=9:
    guess_number=int(input("enter guess number:"))
    if guess_number<n:
        print("enter number is less than ",n)
    elif guess_number>n:
        print("enter number is more than ",n)
    else:
        print("guess correct")
        print("It took",number_of_guesses,"number_of_guesses to guess")
        break
    print("number of guesses left",9-number_of_guesses)
    number_of_guesses=number_of_guesses+1
if number_of_guesses>9:
    print("game over")
     

    

