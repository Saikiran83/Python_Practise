def gettime():
    import datetime
    return datetime.datetime.now()


def log():
    print("Choose your client \n")
    
    client = int(input("1. Harry \n2. Rohan \n3. Hammad "))
    con = 1
    if client == 1:
        while con == 1:
            print("What do you want to log for Harry?")
            choice = int(input("1. Diet \n2. Activity"))
            if choice == 1:
                f = open("harry diet.txt", "a")
                data = input("Enter what has Harry Eaten?")
                f.write(str([str(gettime())]) + "  " + data + "\n")
                f.close()

            else:
                f = open("harry exercise.txt", "a")
                data = input("How much time has Harry worked out?")
                f.write(str([str(gettime())]) + "  " + data + "\n")
                f.close()
            con = int(input("Do you want to log more for Harry? \n1. Yes \n2. No"))

    elif client == 2:
        while con == 1:
            print("What do you want to log for Rohan?")
            choice = int(input("1. Diet \n2. Activity"))
            if choice == 1:
                f = open("rohan diet.txt", "a")
                data = input("Enter what has Rohan Eaten?")
                f.write(str([str(gettime())]) + "  " + data + "\n")
                f.close()

            else:
                f = open("rohan exercise.txt", "a")
                data = input("How much time has Rohan worked out?")
                f.write(str([str(gettime())]) + "  " + data + "\n")
                f.close()
            con = int(input("Do you want to log more for Rohan? \n1. Yes \n2. No"))

    elif client == 3:
        while con == 1:
            print("What do you want to log for Hammad?")
            choice = int(input("1. Diet \n2. Activity"))
            if choice == 1:
                f = open("hammad diet.txt", "a")
                data = input("Enter what has Hammad Eaten?")
                f.write(str([str(gettime())]) + "  " + data + "\n")
                f.close()

            else:
                f = open("hammad exercise.txt", "a")
                data = input("How much time has Hammad worked out?")
                f.write(str([str(gettime())]) + "  " + data + "\n")
                f.close()
            con = int(input("Do you want to log more for Hammad? \n1. Yes \n2. No"))


def retrieve():
    con = 1
    while con == 1:
        print("Choose your client")
        client = int(input("1. Harry \n2. Rohan \n3. Hammad"))
        if client == 1:
            print("What do you want to retrieve for Harry?")
            choice = int(input("1. Diet \n2. Activity"))
            if choice == 1:
                f = open("harry diet.txt", "r")
                print(f.readlines())
                f.close()

            else:
                f = open("harry exercise.txt", "r")
                print(f.readlines())
                f.close()

        elif client == 2:
            print("What do you want to retrieve for Rohan?")
            choice = int(input("1. Diet \n2. Activity"))
            if choice == 1:
                f = open("rohan diet.txt", "r")
                print(f.readlines())
                f.close()

            else:
                f = open("rohan exercise.txt", "r")
                print(f.readlines())
                f.close()

        elif client == 3:
            print("What do you want to retrieve for Hammad?")
            choice = int(input("1. Diet \n2. Activity"))
            if choice == 1:
                f = open("hammad diet.txt", "r")
                print(f.readlines())
                f.close()

            else:
                f = open("hammad exercise.txt", "r")
                print(f.readlines())
                f.close()
    con = int(input("Do you want to retrieve any more details? \n1. Yes \n2. No"))


print("Welcome to Health care Management System")
ch = int(input("What do you want to do? \n1. Log \n2. Retrieve"))
if ch == 1:
    log()
elif ch == 2:
    retrieve()
else:
    print("Wrong Input. Please try again.")