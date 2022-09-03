# if abstract class contain only abstract methods -- interface 
from abc import *
class DBinterface(ABC):
    @abstractmethod
    def connect(self):
        pass
    def disconnect(self):
        pass
class oracle(DBinterface):
    def connect(self):
        print("connecting to oracle DB...")
    def disconnect(self):
        print("disconnecting oracle DB...")
class Sybase(DBinterface): 
    def connect(self): 
        print('Connecting to Sybase Database...') 
    def disconnect(self): 
        print('Disconnecting to Sybase Database...') 
dbname=input('Enter Database Name:') 
classname=globals()[dbname] 
x=classname() 
x.connect() 
x.disconnect()
# Note: The inbuilt function globals()[str] converts the string 'str' into a class name and 
# returns the classname