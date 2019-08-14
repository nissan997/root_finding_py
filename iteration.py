import math
#g(x) of the function f(x)
def g(x):
    result=(math.cos(x)+1)/3
    return (result)
def iteration(guess,tol):
    result=0
    a=g(guess)
    b=g(a)
    n=100
    for i in range(0,n):
        if(round(a,tol)==round(b,tol)):
            result=a
            break
        else:
            a=b
            b=g(b)
    return result
tol=int(input("Enter the tolarence in decimal places:"))
answer = iteration(3.2,tol)
print('answer:',round(answer,tol))
