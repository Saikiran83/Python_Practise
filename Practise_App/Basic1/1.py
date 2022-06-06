####### GET PYTHON VERSION #############
import sys 
print("python version")
print(sys.version)
print("version info")
print(sys.version_info)

####### PRINT CURRENT DATE & TIME ##########
import datetime
now = datetime.datetime.now()
print("current date % time is :")
print(now.strftime("%Y-%m-%d %H:%M:%S"))

###### RADIUS OF CIRCLE ######
from math import pi
r = float(input("enter radius :"))
print("area of circle with" + str(r) + "is" + str(pi*r**2))

#############(01,06,2022) to 01/06/2022 ########
exam_date = (1,6,2022)
print("exam date is:%i / %i/ %i"%exam_date)

###############calendar ############
import calendar 
y = int(input("enter year:"))
m = int(input("enter month:"))
print(calendar.month(y,m))

##### multi doc ######
print(""" hi "sai" how r u """)

######## no of dates bw two dates ###
from datetime import date
f = date(2014,7,2)
l = date(2014,7,12)
delta = l - f 
print(delta )

######## n copies of given string ###### 
def copies(str,n):
    res = ""
    for i in range(n):
        res = res + str
    return res 
print(copies('sai',2))

######count in list ######
#or count = 0
    # for num in nums:
    #     if n = num:
    #         count = count +1 
    # return count 
        
def list_count(n,nums):
    return nums.count(n)
print(list_count(2,[2,2,2,2,2,5,5,]))
    
##### n copies of given first 2 ch of given str, if len(str) <2 then n copies of whole str #

def n_copies(str,n):
    l = 2
    if l > len(str):
        l =len(str)
    substr = str[:l]
    res = ''
    for i in range(n):
        res = res + substr
    return res
print(n_copies('sai',3))

###passed letter is vowel or not ##
def vowel(char):
    all_vowels = 'aeiou'
    return char in all_vowels
print(vowel('a'))

##specific value in group of values ###
def group(grp,n):
    for value in grp :
        if value == n :
            return True
    return False 
print(group([1,2,3,4],2))

##histogram for items in list ####
def hist(items):
    for n in items:
        output = ''
        times = n
        while(times > 0):
            output = output + '*'
            times = times -1 
        print(output)
print(hist([1,2,3]))