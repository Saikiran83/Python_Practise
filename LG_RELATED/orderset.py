#like set (unique elements) but in set there is no order
# in orderset order is preserved 
from ordered_set import OrderedSet
bankStatement = OrderedSet(["BK0001","BK0002","BK0003","BK0004","BK0005"])
print("Transaction no",bankStatement[1],"has been recorded successfully")
bankStatement.add("BK0004")
print(bankStatement)

from ordered_set import OrderedSet
bankStatement1 = OrderedSet(["BK0001","BK0002","BK0003","BK0004","BK0005"])
bankStatement2 = OrderedSet(["BK0004","BK0005","BK0006","BK0007","BK0008"])
 
diff  = bankStatement1 - bankStatement2
print("The transactions unique to the first summary are",list(diff))
 
inter = bankStatement1 & bankStatement2
 
print("The transactions common to both summary are",list(inter))
 
union = bankStatement1 | bankStatement2
 
print("Here are all the transactions of these summaries:",list(union))