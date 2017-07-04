from Stack import Stack
def decTobin(num):
    l=[]
    s=Stack()
    flag=True
    while flag:
        num,r=divmod(num,2)
        s.push(r)
        while num>1:
            num,r=divmod(num,2)
            s.push(r)
        flag=False
    num,r=divmod(num,2)
    s.push(r)

    while s.isEmpty()!=True:

        l.append((s.pop()))
    return "".join(map(str,l))




binary=decTobin(5)
print(binary)
