def insertion(seq):
    for index in range(1,len(seq)):
        current=seq[index]
        pos=index
        while pos>0 and seq[pos-1]>current:
            seq[pos]=seq[pos-1]
            pos-=1
        seq[pos]=current
    return seq
x=insertion([54,26,93,17,77,31,44,55,20])
print(x)