
def find(num):
    
    sortedList = sorted(num)
    
    newList = []
    for value in sortedList:
        if value not in newList:
            newList.append(value)
    print("list ", newList)
        
    









find([2, 4 , 1, 4, 7, 4, 6])
