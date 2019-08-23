import random
import time

#######################
# Sorting Algorithms  #
#######################


# Adapted from wikipedia psuedo code
# Should have approximately nlog(n) complexity
def mergesort(list):
    if len(list)>1:
        # Finds middle of list
        middle=len(list)//2
        # Seperates list into two halves
        first=list[:middle]
        second=list[middle:]
        # Recursive call of both halves
        first=mergesort(first)
        second=mergesort(second)
        # Temporary List
        result=[]
        # While the list are no empty
        while len(first)>0 and len(second)>0:
            # Appends smaller value to result
            if first[0]<second[0]:
                result.append(first.pop(0))
            else:
                result.append(second.pop(0))
        # Adds any left over values from either list
        while len(first)>0:
                result.append(first.pop(0))
        while len(second)>0:
                result.append(second.pop(0))
        return result
    else:
        return list

# Should have approximately n^2 complexity
def selectionsort(list):
    # Temporary list
    sorted=[]
    # As long as the list is not empty
    if len(list)>1:
        # Pops the minimum value to the temporary list
        sorted.append(list.pop(list.index(min(list))))
        # Recursive call on the rest of the list
        sorted.extend(selectionsort(list))
        return sorted
    else:
        return list

#######################
# Sorting Tests       #
#######################

testList=[8,9,6,5,0,7,2,7,5,1,9,6,10]

# Mergesort test
mergesort(testList)

# Selectionsort test
selectionsort(testList)


########################
# Algorithm Comparison #
########################


# Creates a list and times both sorting functions
# n: the length of the list
def sort_tester(n=10):
    # List to hold times of function calls
    results=[]
    # Temp list to be sorted
    test_list=[]

    # Creates a list of length n and then shuffles it
    for j in range(0,n):
        test_list.append(j)
    random.shuffle(test_list)

    # Tests and times Mergesort
    start = time.time()
    mergesort(test_list)
    end = time.time()
    results.append(100*(end-start))

    #Tests and times Selectionsort
    start = time.time()
    selectionsort(test_list)
    end = time.time()
    results.append(100*(end-start))

    return results



# Calls sort test for list of incrementally increasing lengths
results={'Merge':[],'Selection':[]}
for i in range(100,2000,100):
    # Temporary list
    temp=sort_tester(i)
    results['Merge'].append(temp[0])
    results['Selection'].append(temp[1])

# Comparison Graphing
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
