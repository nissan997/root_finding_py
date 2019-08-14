import math
def f(x):
    return(3*x -math.cos(x)-1) #the function
def fp(x):
    return(3+math.sin(x))
def midfunc(x0):
    x1=x0-(f(x0)/fp(x0))
    return(x1)
def newrap_method(a,b,tol):
    if f(a)*f(b)>0:
        print("No root found.")
    else:
        x0=a
        x1=midfunc(x0)
        if(round(x0,tol)==round(x1,tol)):
            return x1
        else:
            x0=x1
            x1=midfunc(x1)
        return(x1)
tol=int(input("Enter decimal places for tolerance:"))
answer=newrap_method(0,1,tol)
print('answer:',round(answer,tol))
