import math
def f(x):
    return(3*x -math.cos(x)-1) #the function
def midpoint(a,b,fa,fb):
    result=((a*fb)-(b*fa))/(fb-fa)
    return(result)
def falsi_method(a,b,tol):
    if f(a)*f(b)>0:
        print("No root found.")
    else:
        while (b-a)/2.0 > tol :
            mid = midpoint(a,b,f(a),f(b))
            if f(mid) == 0:
                return (mid) #root
            elif f(a)*f(mid)<0:
                b= mid
            else :
                a= mid
        return(mid)
answer = falsi_method(-1,5,0.01) #(a,b,tolerance)
print("Answer: ",round(answer,3))
