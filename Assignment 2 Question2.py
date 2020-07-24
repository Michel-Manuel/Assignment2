from numpy import random #This module would be used for all random number generations


import datetime #This module would be used to calculate the time fot execution  


"""This next block of code recieves the sizes of the arrays going to be used for the program"""
N= int(input("Size of array: ")) 
N2 = int(input("Second Size of array: "))
N3 = int(input("Third Size of array: "))


BinaryTime=[]
InterpolationTime=[]
myList =[]

for i in range(N):
    value =random.randint(1,32767)
    myList.append(value)
myList.sort()
for i in range(N2):
    value =random.randint(1,32767)
    myList.append(value)
myList.sort()
for i in range(N3):
    value =random.randint(1,32767)
    myList.append(value)
myList.sort()
start_time = datetime.datetime.now()

#This function find an element/number in an array using the interpolationsearch method
def InterpolationSearch(array, low, high, target):
    
    low=0
    
    position = (low + (( (high - low) * (target - array[low])) // (array[high] - array[low])))
    while target != array[position] :
        if array[position] < target :
            high = position - 1
            
            position = (low + (( (high - low) * (target - array[low])) // (array[high] - array[low])) )
        else :
            low = position +1
            position = (low + (( (high - low) * (target - array[low])) // (array[high] - array[low])))          
    
    


    end_time = datetime.datetime.now()
    time_diff = (end_time - start_time)*1000#Calculates the exucution time of this function 
    
    print("Time used for Interpolation Search", time_diff.total_seconds() )
    InterpolationTime.append( time_diff.total_seconds())      
        

start_time = datetime.datetime.now()

#This function find an element/number in an array using the Binary Search method
def BinarySearch(arr, low, high, target):
    
  
    
    if high >= low: 
  
        mid = (high + low) // 2
  
       
        if arr[mid] == target:
            end_time = datetime.datetime.now()
            time_diff = (end_time - start_time) *1000#Calculates the exucution time of this function 
            
            print("Time used for Binary Search", time_diff.total_seconds() ) 
            BinaryTime.append(time_diff.total_seconds())
            
  
         
        elif arr[mid] > target: 
            return BinarySearch(arr, low, mid - 1, target) 
  
        # Else the element can only be present in right subarray 
        else: 
            return BinarySearch(arr, mid + 1, high, target)   


        
        
   


target=random.choice(myList)
print(target)
BinarySearch(myList, 0, len(myList)-1, target)
InterpolationSearch(myList, 0, len(myList)-1, target)

TotalBinaryTime = sum(BinaryTime)/len(BinaryTime)
TotalInterpolationTime = sum(InterpolationTime)/len(InterpolationTime)
print("Average Binary Time", TotalBinaryTime)
print("Average Interpolation Time",TotalInterpolationTime)



    












  
  



 




