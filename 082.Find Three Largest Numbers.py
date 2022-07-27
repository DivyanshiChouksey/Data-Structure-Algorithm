# Find Three Largest Numbers
"""
    So basically we'll keep track and store three largest numbers by initialising an empty array 
    and by going through the array if we will found greater number than any of three largest numbers
    then by shifting the numbers too thier left we put the smallest number out of the array and store the greatest number  
    
"""
# Time Complexity = O(n) || Space Complexity = O(n)

array = [55, 7, 8, 3, 43, 11]


def findThreeLargestNumbers(array):
    threeLargest = [float("-inf"), float("-inf"), float("-inf")]
    for num in array:
        if num > threeLargest[2]:
            threeLargest[0] = threeLargest[1]
            threeLargest[1] = threeLargest[2]
            threeLargest[2] = num

        elif num > threeLargest[1]:
            threeLargest[0] = threeLargest[1]
            threeLargest[1] = num
        elif num > threeLargest[0]:
            threeLargest[0] = num
        else:
            continue
    return threeLargest


print(findThreeLargestNumbers(array))
