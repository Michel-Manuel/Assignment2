
class Deque():
    def __init__(self, myList):
        
        self.myList= myList
        

    def isEmpty(self):
        if self.myList == [] :
        
            return True
        else :
            return False 

    def addFront(self,item):
        self.myList.append(item)
        
    def addRear(self,item):
        self.myList.insert(0,item)

    def removeFront(self):
        return self.myList.pop()

    def removeRear(self):
        self.myList.pop(0)
        
from numpy import random
x= random.randint(100, size =(20))
print(x)

middle = len(x)//2
half = x[:middle]
x = half
print(x)
myDeque = Deque(x)

while myDeque.isEmpty() == False and len(x) != 20:
    randomValue =round(random.uniform(0,1),1)
    
    if randomValue == 0.1 :
        myDeque.addFront(randomValue)

    elif randomValue ==0.2:
        myDeque.removeFront()

    elif  randomValue == 0.4:
        myDeque.addRear(randomValue)
        
    elif randomValue == 0.6:
        myDeque.removeRear()

    

         
        
        
        
        




 



 
