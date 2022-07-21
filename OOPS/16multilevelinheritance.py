class dad:
    games = 3
class son(dad):
    games = 5
    dance = 3
    def isdance(self):
        return f"i dance {self.dance} no of times"
class grandson(son):
    games = 6 
    dance = 7
    def isdance(self):
        return f" i dance {self.dance} no of times for sure"
harry = dad()
larry = son()
varry = grandson()
print(varry.games) ## it will take grandson 
#if it is not there then it will look in son 
print(varry.isdance())
