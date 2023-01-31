# 132 Pattern

"""
    There are alot of ways to solve this question
    
    # Naive Solution 
        With 3 for loop and check 132 pattern

    # Optimized SOlution
        Using of stack in single pass (1,3,2 -> s1,s2,s3)
        Main idea - all values in tha stack are candidates for s2
        it stores the values in decreasing order , as smaller values will be popped out and 
        assigned to s3 before the new value is appended to the stack.

        steps :-
        1. Initilaize s3 a variable as negative infinity and a empty stack 
        2. Do a for loop in reverse order, current value(n) will be candidate for s1
        3. If n < s3 , it will also < s2, since s3 < s2 return True
        4. If stack[-1] is less than n, we have a new candidate for s3 pop all the values smaller than n 
           (which will be the candidate for s2) in the stack and update s3(it will be the largest possible s3.)
        5. Else append it in stack
        6. Outside the loop return False.
"""

# Time Complexity = O(n)  , 2n = n =>n for appending values and n for popping out the values
# Space COmpleixty = O(n)

nums = [3,1,4,2]

def find132pattern(nums):
    stack = []
    s3 = float("-inf")
    for n in nums[::-1]:   
        if n < s3 :
            return True
        while len(stack) and stack[-1]<n: 
            s3 = stack.pop()
        
        stack.append(n)
    return False

print(find132pattern(nums))
