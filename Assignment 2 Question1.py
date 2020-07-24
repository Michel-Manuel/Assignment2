class Deque():
    def __init__(self):
        
        self.items=[]
        

    def isEmpty(self):
        if self.items == [] :
        
            return True
        else :
            return False 

    def addFront(self,item):
        self.items.append(item)
        return self.items
        
    def addRear(self,item):
        self.items.insert(0,item)
        return self.items

    def removeFront(self):
        self.items.pop()
        return self.items

    def removeRear(self):
        self.items.pop(0)
        return self.items


"""
The next set of code would keep removing and adding random numbers to the deque , based on a a random probabilty  generator,
till the length of the Deque gets to 20 
"""
from numpy import random
x= random.randint(100, size =(20))

print("Original Deque: ", x)
middle = len(x)//2
half = x[:middle]
x = list(half)
print("Instance of half-full Deque: " , x)
myDeque = Deque()

for i in range(len(x)):
    myDeque.addFront(i)


while len(x) != 20 :
    randomValue =round(random.uniform(0,1),1)
    print("Random Value: ", randomValue)
    
    if myDeque.isEmpty()== True :
        myDeque.addFront(randomValue)
        
    elif len(x) == 0:
        x.append(randomValue)   

    
        
    elif 0 < randomValue <= 0.1 :
        myDeque.addFront(randomValue)
        x.append(randomValue)

    elif 0.1 < randomValue <= 0.3:
        myDeque.removeFront()
        x.pop()
        
        

    elif  0.3 < randomValue <= 0.4:
        myDeque.removeRear()
        
        
        x.pop(0)
        
        
    elif 0.4 < randomValue <= 1:
        
        x.insert(0,randomValue)
        myDeque.addRear(randomValue)
        
        
print(myDeque)
print(x)
        







    

         
        
        
        
        




 



 
