"""def bSearch(seq,key):
    mid=0
    last=len(seq)-1
    found=False
    first=0
    while first<=last and not found:
        mid=(first + last)//2
        if seq[mid]==key:
            print("Key found at index:",mid)
            found=True
        elif seq[mid]>key:
            last=mid-1
        else:
            first=mid+1
    if found==False:
        print("Searching stopped at",mid)
bSearch([1,3,6,9,12,15,43],12)"""
#Recursively Calling bSearch

def brsearch(seq,key):
    mid=0
    if len(seq)==0:
        return False
    else:
        mid==len(seq)//2
        if seq[mid]==key:
            return True
        elif seq[mid]<key:
            return brsearch(seq[mid + 1:],key)
        else:
            return brsearch(seq[:mid],key)


print(brsearch([1,2,4,6,8,12,18,34],13))
