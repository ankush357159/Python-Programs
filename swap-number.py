#Python program to swap first and last number of an array
#Swap Function
def swapList(newList):
    size = len(newList)

    #swapping
    temp = newList[0]
    newList[0] = newList[size -1]
    newList[size - 1] = temp

    return newList

#Driver code
newList = [12,10,15,30,25,55]

print(swapList(newList))