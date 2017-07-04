class Queue:
    def __init__(self):
        self.items=[]
    def isEmpty(self):
        return self.items==[]

    def enQueue(self,item):
        self.items.insert(0,item)
    def deQueue(self):
        if self.isEmpty():
            print("Queue Empty")
        else:
            return self.items.pop()
    def size(self):
        return len(self.items)
    def show(self):
        print(self.items)

