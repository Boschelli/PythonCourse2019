import random
import time

# Adapted from wikipedia suedo code
def mergesort(list):
    if len(list)>1:
        middle=len(list)//2
        first=list[:middle]
        second=list[middle:]
        first=mergesort(first)
        second=mergesort(second)
        result=[]
        while len(first)>0 and len(second)>0:
            if first[0]<second[0]:
                result.append(first.pop(0))
            else:
                result.append(second.pop(0))
        while len(first)>0:
                result.append(first.pop(0))
        while len(second)>0:
                result.append(second.pop(0))
        return result
    else:
        return list

def selectionsort(list):
    sorted=[]
    if len(list)>1:
        sorted.append(list.pop(list.index(min(list))))
        sorted.extend(selectionsort(list))
        return sorted
    else:
        return list

def sort_tester(n=10,increment=1):
    for i in range(1,n+1,(n//increment)):
        test_list=[]
        for j in range(0,i):
            x = random.randint(1,10)
            test_list.append(x)






mergesort(testlist)
selectionsort(testlist)
