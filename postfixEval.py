from Stack import Stack
def postEval(postexp):
    evalStack=Stack()
    tokenList=postexp.split()
    for token in tokenList:
        if token in "1234567890":
            evalStack.push(int(token))
        else:
            operand2=evalStack.pop()
            operand1=evalStack.pop()
            result=doCal(token,operand1,operand2)
            evalStack.push(result)
    return evalStack.pop()
def doCal(exp,x,y):
    if exp=="+":
        return x+y
    elif exp=="-":
        return x-y

    elif exp=="/":
        return x/y
    elif exp=="**":
        return x**y

    else:
        return x*y

print(postEval("5 3 4 2 - ** *"))