# Pow(x, n)

x = 2.00000
n = 10


def myPow(x, n):
    if n==0:
        return 1
    if n<0:
        return 1/(myPow(x,-n))
    if n % 2:
        return x * myPow(x, n-1)
    return myPow(x*x, n/2)


print(myPow(x, n))
