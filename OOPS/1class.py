class student:
    def __init__(self,name,age,profession):
        self.name = name 
        self.age = age
        self.profession = profession
    
    def talk(self):
        print("hello my name is:",self.name)
        print("my age is:",self.age)
        print("my job is:",self.profession)
s = student('sai',24,'analyst')
s.talk()
###########################
class sai:
    def __init__(self):
        print('constructor called')
s = sai()
