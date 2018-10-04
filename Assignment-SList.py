class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Slist:
    def __init__(self,value):
        node = Node(value)
        self.head = node

    def addNode(self,value):
        node = Node(value)
        runner = self.head
        while(runner.next != None):
            runner = runner.next
        runner.next = node

    def printAllValues(self):
        runner = self.head
        while(runner.next != None):
            print(runner.value)
            runner = runner.next
        print(runner.value)


# part 2
    def removeNode(self,value):
        runner = self.head
        if(self.head.value == value):
            self.head =runner.next
        else:
            prevnode=0
            nextnode=0
            while(runner.next != None):
                prevnode = runner
                runner = runner.next
                nextnode = runner.next
                if(runner.value == value):
                    prevnode.next = nextnode


# part 3    
    def insertNode(self, value, index):
        node= Node(value)
        if(index == 0):
            node.next = self.head
            self.head = node
            return self
        runner = self.head
        # for x in range(index -1):
        #     runner = runner.next
        # node.next = runner.next
        # runner.next = node
        while(runner.next != None):

            runner= runner.next
            count += 1
            if(count == index):
                node.next = runner.next
                runner.next = node
                return self



    

print("\n\n\n\n================== START OF THE PROGRAM ================")       
# list = Slist(2)
# list.addNode(3)
# list.addNode(5)
# list.addNode(6)
# list.addNode(7)
# list.removeNode(4)
# list.printAllValues()

list = Slist(5)
list.addNode(7)
list.addNode(9)
list.addNode(1)
list.removeNode(9) # removes 9, which is one of the middle nodes in the list
list.removeNode(5) # removes 5, which is the first value in the list
list.removeNode(1) # removes 1, which is the last node in the list
list.printAllValues()
