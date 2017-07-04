from Stack import Stack


def parChecker(sequence):
    s=Stack()
    Balanced=True
    index=0
    while index<len(sequence) and Balanced:
        symbol=sequence[index]
        if symbol=="(":
            s.push(symbol)
        else:
            if s.isEmpty():
                Balanced=False
            else:
                s.pop()
        index+=1
    if Balanced and s.isEmpty():
        print("The sequence is Balanced")
    else:
        print("The sequence is unbalanced")

def main():
    seq=input("Enter a sequence")
    parChecker(seq)
if __name__=='__main__':
    main()


