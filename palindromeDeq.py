from deQueue import dequeue
def palindrome(exp):

    d=dequeue()
    plist=list(exp)
    for i in plist:
        d.addRear(i)
    flag=True
    while flag and len(d.items)>=1:
        if d.delRear()==d.delFront():
            pass
        else:
            flag=False
    if len(d.items)==1 or len(d.items)==0:
        print("The string is a Palindrome")
    else:
        print("The string is not a Palindrome")

palindrome("naman")

