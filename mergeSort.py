def mergesort(seq):
    n=len(seq)
    if n==1:
        return seq
    else:
        mid=len(seq)//2
        left=seq[:mid]
        right=seq[mid:]

        mergesort(left)
        mergesort(right)


        merge(left,right,seq)

def merge(l,r,seq):
    i=0
    j=0
    k=0
    nl=len(l)
    nr=len(r)
    while i<nl and j<nr:
        if l[i]<=r[j]:
            seq[k]=l[i]
            i=i+1
        else:
            seq[k]=r[j]
            j=j+1
        k=k+1
    while i<nl:
        seq[k]=l[i]
        i=i+1
        k+=1
    while j<nr:
        seq[k]=r[j]
        j=j+1
        k+=1
    print("nu",seq)




mergesort([2,4,1,6,5,8,3,9,7,10])