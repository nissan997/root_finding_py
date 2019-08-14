import math
def f(x):
    return(3*x -math.cos(x)-1) #the function
def bisection_method(a,b,tol):
    if f(a)*f(b)>0:
        print("No root found.")
    else:
        while (b-a)/2.0 > tol :
            midpoint = (a+b)/2.0
            if f(midpoint) == 0:
                return (midpoint) #root
            elif f(a)*f(midpoint)<0:
                b= midpoint
            else :
                a= midpoint
        return(midpoint)
answer = bisection_method(-1,5,0.0001) #(a,b,tolerance)
print("Answer: ",round(answer,3))
