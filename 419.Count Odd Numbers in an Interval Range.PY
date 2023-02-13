# Count Odd Numbers in an Interval Range

"""
    Maths trick :-
        0-100 = contains 50 odd
        1-100 = contains 50 odd ---> 99/2 = 49 , 49+1 = 50 
        if high or low is odd then return (high-low)/2+1 else return (high-low)/2
"""

# Time Complexity = O(1) || Space Complexity = O(1)

low = 3
high = 7

def countOdds( low, high):
    if high%2==1 or low%2==1:
        return (high-low)//2 + 1
    return (high-low)//2

print(countOdds( low, high))