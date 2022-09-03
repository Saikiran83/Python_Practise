from abc import * 
class Printer(ABC): 
    @abstractmethod 
    def printit(self,text):pass 
    @abstractmethod 
    def disconnect(self):pass 
class EPSON(Printer): 
    def printit(self,text): 
        print('Printing from EPSON Printer...') 
        print(text) 
    def disconnect(self): 
        print('Printing completed on EPSON Printer...')  
class HP(Printer): 
    def printit(self,text): 
        print('Printing from HP Printer...') 
        print(text) 
    def disconnect(self): 
        print('Printing completed on HP Printer...') 
with open('config.txt','r') as f: 
    pname=f.readline() 
classname=globals()[pname] 
x=classname() 
x.printit('This data has to print...') 
x.disconnect() 
