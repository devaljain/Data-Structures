class Node:
    def __init__(self,data):
        self.data=data
        self.link=None

    def getData(self):
        return self.data
class linkedList:
    def __init__(self):
        self.head=None

    def insertFront(self,data):
        ob=Node(data)
        if self.head==None:
            self.head=ob
        else:
            temp=self.head
            self.head=ob
            ob.link=temp

    def insertPos(self,data,pos):
        new=Node(data)
        ptr=self.head
        for i in range(pos-1):
            ptr=ptr.link
            if(ptr==None):
                print("Index out of memory")
                break
            else:
                continue
        temp=ptr.link
        new.link=temp
        ptr.link=new

    def insertEnd(self,data):
        new=Node(data)
        ptr=self.head
        if(self.head)==None:
            self.head=new
        else:
            while ptr.link!=None:
                ptr=ptr.link
            ptr.link=new

    def delStart(self):
        if self.head==None:
            print("Empty List")
        else:
            temp=self.head
            self.head=temp.link

    def show(self):
        if self.head==None:
            print("No nodes")
        else:
            q=self.head
            while q!=None:

                print(q.data, end=" ")
                q=q.link
    def delPos(self,pos):
        ptr=self.head
        for i in range(1,pos-1):
            ptr=ptr.link
            if ptr==None:
                print("Out of indexed memory")
                break
            else:
                continue
        temp=ptr.link
        ptr.link=temp.link

    def delEnd(self):
        ptr=self.head
        if(ptr==None):
            print("List Empty")
        else:
            while ptr.link!=None:
                temp=ptr
                ptr=ptr.link
            temp.link=None
            #The end node is destroyed automatically by the garbage collector because it is
                              #not reachable
    def search(self,data):
        ptr=self.head
        found=False
        while not found and ptr!=None:
            if ptr.getData()==data:
                found=True
            else:
                ptr=ptr.link
        return found








lep=linkedList()
lep.insertFront(5)
lep.insertFront(6)
lep.insertFront(8)



lep.show()
print(lep.search(6))
print(lep.search(2))

