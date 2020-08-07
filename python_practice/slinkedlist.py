class Node:
    # def __init__(self, dataval=None):
    #     self.dataval = dataval
    #     self.nextval = None
    def __init__(self, dataval):
        self.dataval = dataval
        self.nextval = None

    def addchartonode(self,char):
        self.dataval = self.dataval + char

class SLinkedList:
    def __init__(self):
        self.headval = None

    def listprint(self):
        printval = self.headval
        while printval is not None:
            print (printval.dataval)
            printval = printval.nextval
    
    def addchar(self,char):
        addval = self.headval
        while addval is not None:
            addval.dataval = addval.dataval + char
            addval = addval.nextval
    
    
        

list = SLinkedList()
list.headval = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")
e4 = Node("Thu")
# Link first Node to second node
list.headval.nextval = e2

# Link second Node to third node
e2.nextval = e3

# link third to second
e3.nextval = e4

# delete node
e3.nextval = None

list.headval = e2

#add char
e2.addchartonode("hello")
list.addchar("hi")
list.listprint()