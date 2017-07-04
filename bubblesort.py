from time import perf_counter
start=perf_counter()

def bubSort(seq):
    lambai=len(seq)
    sorted=True
    while lambai>0 and sorted:
        sorted=False
        for i in range(lambai-1):
            if seq[i]>seq[i+1]:
                sorted=True
                temp=seq[i]
                seq[i]=seq[i+1]
                seq[i+1]=temp
            else:
                pass
        lambai=lambai-1
    return seq
print(bubSort([54,26,93,17,77,31,44,55,20,21]))
print(perf_counter()-start)


