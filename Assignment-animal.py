class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Slist:
    def __init__(self, value):
        node = Node(value)
        self.head = node

    def addNode(self, value):
        runner = self.head
        node = Node(value)
        while( runner.next != None):
            runner = runner.next 
        runner.next = node

    def printallvalues(self):
        runner = self.head
        while(runner.next != None):
            print(runner.value)
            runner = runner.next
        print(runner.value)

    def removeval(self,value):
        runner = self.head
        if(self.head.value == value):
            self.head = runner.next
        else:
            prevnode = 0
            nextnode = 0
            while(runner.next != Node):
                prevnode = runner
                runner = runner.next
                nextnode = runner.next
                if(runner.value == value):
                    prevnode.next = runner.next
                    return self




list = Slist(1)
list.addNode(2)
list.addNode(3)
list.addNode(4)
list.addNode(5)
list.addNode(6)
list.removeval(5)
list.printallvalues()
            
