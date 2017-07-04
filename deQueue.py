class dequeue:

    def __init__(self):
        self.items=[]

    def isEmpty(self):
        return len(self.items)==0

    def addFront(self,item):
        self.items.append(item)
    def addRear(self,item):
        self.items.insert(0,item)
    def delFront(self):
        if self.isEmpty():
            return "Dequeue Empty"
        else:
            self.items.pop()
    def delRear(self):
        self.items.pop(0)
    def size(self):
        print(len(self.items))
    def show(self):
        print(self.items)

