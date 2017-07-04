from Queue import Queue

def hotPoatato(num):

    q=Queue()
    q.enQueue("Deval")
    q.enQueue("Naman")
    q.enQueue("Shubhi")
    q.enQueue("Vinny")
    q.enQueue("Aakriti")
    q.enQueue("Mahesh")
    print(q.items)
    while q.size()>1:
        i=0
        while i<num:
            x=q.deQueue()
            q.enQueue(x)
            i+=1
        q.deQueue()
    print(q.show())
hotPoatato(7)
