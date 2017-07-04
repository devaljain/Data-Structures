def quicksort(seq):
    sorthelp(seq,0,len(seq)-1)

def sorthelp(A,start,end):
    if start<end:
        pindex=partition(A,start,end)
        sorthelp(A,pindex+1,end)
        sorthelp(A,start,pindex-1)


def partition(A,start,end):
    pindex=start
    pivot=A[end]
    for i in range(start,end):
        if A[i]<=pivot:
            temp=A[i]
            A[i]=A[pindex]
            A[pindex]=temp
            pindex+=1
    temp=A[pindex]
    A[pindex]=A[end]
    A[end]=temp
    return pindex
x=[2,4,6,1,3,5]
quicksort(x)
print(x)