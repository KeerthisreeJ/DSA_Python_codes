from math import inf

from numpy import Inf

s = int(input("Enter the search number : "))

array = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,Inf]
def BS(low, s,high):
    mid = round((low+high)/2)

    if s == array[mid]:
        return ("found")
    
    elif s < array[mid]:
        high = mid
        return BS(low,s,high)
    
    elif s>array[mid]:
        low = mid
        return(low,s,high)
    else :
        print("not found")

for i in range (1,len(array)):
    if (s == 2**0):
        print("found")
    elif (s<=2**i and s>=2**(i-1)):
        BS(2**(i-1),s,2**i)
        break
    else :
        continue

    



