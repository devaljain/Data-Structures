class Node:
    def __init__(self,data):
        self.data=data
        self.link=None

class UnOrdered:
    def __init__(self):
        self.head=None

    def add(self,data):
        new=Node(data)
        ptr=self.head
        stop=False
        temp=None

        while ptr!=None and not stop:
            if ptr.data<data:
                stop=True
            else:
                temp=ptr
                ptr=ptr.link
        n=Node(data)
        if temp==None:
            n.link=self.head
            self.head=n
        else:
            n.link=ptr
            temp.link=n


    def show(self):
        if self.head==None:
            print("No nodes")
        else:
            q=self.head
            while q!=None:

                print(q.data, end=" ")
                q=q.link

ul=UnOrdered()
ul.add(3)
ul.add(5)
ul.add(4)
ul.add(11)
ul.add(10)
ul.add(1)
ul.show()