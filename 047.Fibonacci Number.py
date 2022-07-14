# Fibonacci Number
"""
    fibonacci series - 0 1 1 2 3 5 8 ...
    basically we are adding pervious two no.for generating current no.
    initially a=0 ,b=1 and the next no. would be a+b = 1 and updating a=b ,b=a+b  

"""
# Time Complexity = O(n) || Space Complexity = O(1)
n=7
if n == 0:
    print("0")
if n== 1:
    print("1")
a=0
b=1
for i in range(n-1):
    next = a+b
    a =b
    b= next
print(next)