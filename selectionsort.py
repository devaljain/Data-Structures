from time import perf_counter
start=perf_counter()
def selsort(seq):
    length=len(seq)
    print(length)
    for i in range(0,length):
        max=0
        for i in range(1,length):

            if seq[i]>seq[max ]:
                max=i

        temp=seq[max]
        seq[max]=seq[length-1]
        seq[length-1]=temp
        length-=1
    return seq


result=selsort([26,54,93,17,77,31,44,55,20])
print(result)
print(perf_counter()-start)