def linearS(seq,key):
    length=len(seq)
    i=0
    found=False
    while i<length and not found:
        if seq[i]==key:
            print("Key found at index:",i)
            found=True
        else:
            i=i+1
def orderedSearch(seq,key):
    length=len(seq)
    found=False
    stop=False
    i=0
    while i<length and not found and not stop:
        if seq[i]==key:
            found=True
            print("Key found at index:",i)
        else:
            if seq[i]>key:
                stop=True
                print("Stopped at:",i)
            else:
                i=i+1




linearS([1,2,3,2,1],2)
orderedSearch([1,3,13,21,33,44],22)