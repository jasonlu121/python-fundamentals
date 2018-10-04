class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None

class Dlist:
    def __init__(self, value):
        node = Node(value)
        self.head = node
        self.tail = node
    
    def printAllValues(self):
        runner = self.head
        while(runner.next != None):
            print(runner.value)
            runner = runner.next
        print(runner.value)
        while(runner.previous != None):
            print(runner.value)
            runner = runner.previous    
        print(runner.value)

    def addNode(self, value):
        node = Node(value)
        headrunner = self.head
        while(headrunner.next != None):
            headrunner = headrunner.next
        headrunner.next = node
        node.previous = headrunner
        self.tail=node
   
    
    def removeNode(self,value):
        runner = self.head
        if(self.head.value == value):
            self.head = runner.next
            runner.next.previous = None
            if(runner.next == None):
                runner = None
                self.head = None
                return self
        elif(self.tail.value == value):
            runner = self.tail
            runner.previous.next = None
            self.tail = runner.previous
            if(runner.previous == None):
                runner = None
                self.tail = None
                return self
        else:
            prevnode=0
            nextnode=0
            while(runner.next != None):
                prevnode = runner
                runner = runner.next
                nextnode = runner.next
                if(runner.value == value):
                    prevnode.next = nextnode
                    nextnode.previous = prevnode

        if (runner.value == value and runner == self.head):
            if(runner.next == None):
                runner = None
                self.head = None
                return self

    def insertNode(self, value, index):
        node= Node(value)
        if(index == 0):
            node.next = self.head
            self.head = node

            return self
        runner = self.head
        for x in range(index -1):
            runner = runner.next
        node.next = runner.next
        runner.next = node
        node.previous = runner
        node.next.previous = node
        


print("\n\n\n\n================== START OF THE PROGRAM ================")       


list = Dlist(5)
list.addNode(7)
list.addNode(9)
list.addNode(1)
list.addNode(11)
list.addNode(12)
list.removeNode(1)
list.removeNode(5)
list.printAllValues()
