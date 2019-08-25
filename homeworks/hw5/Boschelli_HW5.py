class LinkedList():


    def __init__(self,value=None):
        # Checks if value is an int or provided
        if type(value) != int:
            print('List Requires A Node Value of Type Int!')
            return
        # Creates list root
        root=Node(value,None)
        self.head=root
        self.tail=root
        self.length=1

    # Allows for list to be indexed like tradtional List
    # NOTE: Only here to make testing easier. Method is not robust to all user inputs
    def __getitem__(self,index):
        if type(index) != int:
            print('Index Must Be Of Type Int!')
            return
        if index == (-1):
            return self.tail
        # Checks if index is within list range
        if index >= self.length or index < 0:
            print("Error Out Of List Range!")
            return
        # Loops through list index number of times
        temp = self.head
        for i in range(index):
            temp = temp.next
        # Returns node at the index place in the list
        return temp

    def __str__(self):
        # Calls formatted list printer
        return(self.printList(self.head))

    def length(self):
        return self.length

    # Base add node method
    def addNode(self,newValue,before=None):
        # Checks if value is valid
        if type(newValue) != int:
            print('Nodes Only Accept Int Values!')
            return
        # If list is empty calls constructor with new value
        if self.length == 0:
            self.__init__(newValue)
            return
        # If no before appends node to end of the list
        if before == None:
            before = self.tail
        # Creates node and adjusts pointers
        newNode = Node(newValue,before.next)
        # Adjusts before node's pointer
        before.setNext(newNode)
        # Adjusts tail pointer
        if before == self.tail:
            self.tail = newNode
        # Increases length
        self.length += 1

    # Adds node after specified node
    # newValue: Int value for node
    # afterNode: Specified node for placement
    def addNodeAfter(self, newValue, afterNode):
        # Checks if user provided a node
        if type(afterNode) != Node:
            print('After Node Must Be Of Type Node!')
            return
        # Checks if specified node is the head
        if afterNode == self.head:
            # Adds node after head pointer
            self.addNode(newValue,before=self.head)
            return
        # Checks if node exists within the list
        if self.findParent(afterNode)!= None:
            # Adds node after specified node
            self.addNode(newValue,before=afterNode)
            return
        else:
            print("That node is not in the list!")

    # Adds node before specified node
    # newValue: Int value for node
    # beforeNode: Specified node for placement
    def addNodeBefore(self, newValue, beforeNode):
        # Checks if value is valid
        if type(newValue) != int:
            print('Nodes Only Accept Int Values!')
            return
        # Checks if user provided a node
        if type(beforeNode) != Node:
            print('Before Node Must Be Of Type Node!')
            return

        # Checks if specified node is the head
        if beforeNode == self.head:
            # Creates new node
            newNode=Node(newValue,beforeNode)
            # Adjusts head pointer
            self.head = newNode
            return
        # Finds parent of the specified node
        parentNode = self.findParent(beforeNode)
        if self.findParent(beforeNode) != None:
            # Creates new node
            newNode=Node(newValue,beforeNode)
            # Adjusts parent pointer
            parentNode.setNext(newNode)
            return

        print('Before Node Not In List!')
        return


    # Removes node from list
    # nodeToRemove: The node the user wants to remove
    def removeNode(self,nodeToRemove):
        # Checks if user provided a node
        if type(nodeToRemove) != Node:
            print('The Node To Remove Must Be Of Type Node!')
            return
        # Checks if removing head
        if nodeToRemove == self.head:
            # Adjusts head pointer
            self.head = self.head.next
            # Checks if list is of length 1
            if nodeToRemove == self.tail:
                # Adjusts tail
                self.tail = None
            # Removes node
            nodeToRemove = None
            # Adjusts list length
            self.length -= 1
            return
        # Finds parent node
        parentNode=self.findParent(nodeToRemove)
        if parentNode != None:
            # Adjusts parent pointer
            parentNode.setNext(nodeToRemove.next)
            # Check to whether to adjust tail pointer
            if nodeToRemove == self.tail:
                self.tail = parentNode
            # Removes node
            nodeToRemove = None
            # Adjust node
            self.length -= 1
            return
        print('Node To Remove Not Within List!')
        return


    # Removes all nodes with specified value
    # value: int of node value
    def removeNodeByValue(self,value):
        # Checks if value is valid
        if type(value)!= int:
            print('The Value To Remove Must Be Of Type Int!')
            return
        # Cycles Through List
        temp=self.head
        # Index for print statement
        i=0
        while temp != None:
            # If node has value remove it
            if temp.value == value:
                self.removeNode(temp)
                i+=1
            temp=temp.next
        print("Removed %d items from the list with value: %d"%(i,value))
        return

    # Prints formatted list
    def printList(self,node):
        # Initiate return string
        result=''
        # Recursively loops through list
        if node != None:
            result += str(node.value) +' --> ' + self.printList(node.next)
            return result
        # Adds NULL pointer to end of print
        else:
            result+='X'
            return result

    # Finds parent node for specified node
    def findParent(self, findNode):
        # Loops through list
        temp=self.head
        while temp.next != None:
            # Returns parent if found
            if temp.next == findNode:
                return temp
            temp=temp.next
        return None

    # Reverses list
    def reverse(self):
        # Holds previous value
        previousNode=None
        # Current node of the loop
        temp=self.head
        # Node past the current value
        tempNext=temp.next
        # Adjusts head value
        self.head=self.tail

        # Loops through list and adjust pointers
        while tempNext!=None:
            # Reverse current node pointer
            temp.setNext(previousNode)
            # Sets previous node to current node
            previousNode=temp
            # Sets current node to next node
            temp=tempNext
            # Sets next value to next value
            tempNext=temp.next
        # Reverses final node
        temp.setNext(previousNode)
        # Adjusts head pointer
        self.head=temp

    # Checks if list has a cycle
    # Kind of a lazy way to detect a cycle, but it works!
    def hasCycle(self):
        # Since printList() is recursive a cycle will cause a max recursion level error
        try:
            self.printList(self.head)
            return False
        except:
            return True


class Node():
    def __init__(self, value=None, next=None):
        self.value=value
        self.next=next
    def __str__(self):
        return str(self.value)
    # A redundent method to set the next value of a node
    def setNext(self,next):
        self.next=next

# Creates List
testList=LinkedList(5)

# Adds Nodes
testList.addNode(5)
testList.addNode(3)
testList.addNode(2)

# Print Statement
print(testList)

# Add After Test
testList.addNodeAfter(9,testList.head)
print(testList)

# Add Before Test
testList.addNodeBefore(17,testList[3])
print(testList)

# Remove Node Test
testList.removeNode(testList.head)
print(testList)

# Remove Nodes by Values
testList.removeNodeByValue(3)
print(testList)

# Reverse Test
testList.reverse()
print(testList)

# hasCycle Test
# Creates Cycle
cycleList=LinkedList(17)
cycleList.addNode(54)
cycleList.head.next.setNext(cycleList.head)
cycleList.hasCycle()


# Error Handling Checks


# List Creation
newList=LinkedList()

# Adding Node
testList.addNode('Five')

# Add After/Before Test
testNode=Node(100)
testList.addNodeAfter(23,testNode)
testList.addNodeBefore(23,'testList.head')

# Remove Node testList
testList.removeNode(testNode)
