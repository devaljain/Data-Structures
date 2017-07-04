import math
from time import perf_counter
start=perf_counter()
def makeChange(cList,amt,cCount,wCount):
    for c in cList:
        coin=c
        index=cList.index(c)
        for i in range(amt+1):
            if coin<=i:
                if cCount[i]>1+cCount[i-coin]:
                    cCount[i]=1+cCount[i-coin]
                    wCount[i]=index
    return cCount[amt]
def printCoins(amt,whichCoin,cList):
    l=[]
    coin=amt
    while coin>0:
        j=whichCoin[coin]
        l.append(cList[j])
        coin=coin-cList[j]
    return l
def main():
    change=13
    coinsCount=[math.inf]*(change+1)
    print(coinsCount)
    coinsCount[0]=0
    whichCoin=[-1]*(change+1)
    coinsList=[7,2,3,6]
    makeChange(coinsList,change,coinsCount,whichCoin)
    result=printCoins(change,whichCoin,coinsList)
    print(result)
main()
print(perf_counter()-start)
