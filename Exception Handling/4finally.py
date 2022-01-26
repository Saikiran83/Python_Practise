#finally Block:
# It is not recommended to maintain clean up code(Resource Deallocating Code or 
#Resource Releasing code) inside try block because there is no guarentee for the 
#execution of every statement inside try block always.
#It is not recommended to maintain clean up code inside except block, because if there 
    #is no exception then except block won't be executed.
#Hence we required some place to maintain clean up code which should be executed 
   #always irrespective of whether exception raised or not raised and whether exception 
#handled or not handled. Such type of best place is nothing but finally block.#
# Hence the main purpose of finally block is to maintain clean up code
##SYNTAX FOR FINALLY
#try:
#    Risky Code
#except:
#    Handling Code
#finally:
#    Cleanup code

#Case-1: If there is no exception
try:
    print("try") 
except: 
    print("except") 
finally: 
    print("finally") 
#Output
#try 
#finally
 
#Case-2: If there is an exception raised but handled
try: 
    print("try") 
    print(10/0) 
except ZeroDivisionError: 
    print("except") 
finally: 
    print("finally") 
#Output
#try 
#except 
#finally
 
#Case-3: If there is an exception raised but not handled
try: 
    print("try") 
    print(10/0) 
except NameError: 
    print("except") 
finally: 
    print("finally") 
#Output
#try 
#finally 
#ZeroDivisionError: division by zero(Abnormal Termination)