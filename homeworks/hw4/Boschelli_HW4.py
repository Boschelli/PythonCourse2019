import random
import time

# Adapted from wikipedia psuedo code
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






def sort_tester(n=10):
    results=[]
    test_list=[]

    for j in range(0,n):
        test_list.append(j)
    random.shuffle(test_list)

    start = time.time()
    mergesort(test_list)
    end = time.time()
    results.append(100*(end-start))

    start = time.time()
    selectionsort(test_list)
    end = time.time()
    results.append(100*(end-start))
    return results

results={'Merge':[],'Selection':[]}
for i in range(100,2000,100):
    temp=sort_tester(i)
    results['Merge'].append(temp[0])
    results['Selection'].append(temp[1])


import matplotlib.pyplot as plt

x = range(100,2000,100) ## # of elements in list
y1 = results['Merge'] ## time
y2 = results['Selection']
plt.subplots_adjust(left = .13, right = .95, top = .9, bottom = .3)
plt.plot(x, y1)
plt.plot(x,y2)
plt.legend(['Merge', 'Selection'], loc = "upper left", prop = {"size":10})
plt.ylabel("Miliseconds")
plt.xlabel("Size of List")
plt.title("The Effect of Different Sort Algorithms on Runtime")
plt.savefig('plot.pdf')


  
