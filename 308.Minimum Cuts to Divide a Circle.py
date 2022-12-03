# Minimum Cuts to Divide a Circle

"""
    If n is even then we use :- A cut that is represented by a straight line that touches 
    two points on the edge of the circle and passes through its center, hence return n/2  
    else for n is odd use :- A cut that is represented by a straight line that touches 
    one point on the edge of the circle and its center, hence return n 
    and edge condition is n==1 return 0 
"""

# Time Complexity = O(1) || Space Complexity = O(1)

n = 9


def numberOfCuts(n):
    if n == 1:
        return 0
    if n % 2 == 0:
        return n // 2
    else:
        return n


print(numberOfCuts(n))
