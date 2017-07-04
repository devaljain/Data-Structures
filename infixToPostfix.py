from Stack import Stack
def infToPost(exp):
    posexp=[]
    opstack=Stack()
    prec={"(":1,"*":3,"+":2,"-":2,"/":3,"**":3}
    tokenList=exp.split()
    print(tokenList)
    for token in tokenList:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "1234567890":
            posexp.append(token)
        elif token =="(":
            opstack.push(token)
        elif token ==")":
            toptok=opstack.pop()
            while toptok!="(":
                posexp.append(toptok)
                toptok=opstack.pop()
        else:
            while(not opstack.isEmpty()) and (prec[opstack.peek()]>prec[token]):
                posexp.append(opstack.pop())
            opstack.push(token)

    while not opstack.isEmpty():
        posexp.append(opstack.pop())
    return " ".join(posexp)

print(infToPost("5 * 3 ** ( 4 - 2 )"))







