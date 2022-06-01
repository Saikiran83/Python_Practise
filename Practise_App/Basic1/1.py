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