# Building Bridges

"""
https://www.geeksforgeeks.org/dynamic-programming-building-bridges/

Consider a 2-D map with a horizontal river passing through its center. 
There are n cities on the southern bank with x-coordinates a(1) … a(n) and n 
cities on the northern bank with x-coordinates b(1) … b(n). You want to 
connect as many north-south pairs of cities as possible with bridges such 
that no two bridges cross. When connecting cities, you can only connect city 
a(i) on the northern bank to city b(i) on the southern bank. Maximum number 
of bridges that can be built to connect north-south pairs with the above 
mentioned constraints.

Input : 6 4 2 1
        2 3 6 5
Output : Maximum number of bridges = 2
Explanation: Let the north-south x-coordinates
be written in increasing order.

1  2  3  4  5  6
  \  \
   \  \        For the north-south pairs
    \  \       (2, 6) and (1, 5)
     \  \      the bridges can be built.
      \  \     We can consider other pairs also,
       \  \    but then only one bridge can be built 
        \  \   because more than one bridge built will
         \  \  then cross each other.
          \  \
1  2  3  4  5  6 

Input : 8 1 4 3 5 2 6 7 
        1 2 3 4 5 6 7 8
Output : Maximum number of bridges = 5
"""

# Solution
"""
    As per the question sort the given input

    Let's assume that every pair in array is a valid bridge so for this creating a sequence array to keep 
    track of max sequence
    go through the array in reverse order from the current element and check for smaller values than 
    current value
    then update sequence of current value with the maximum of sequence value and current 
    sequence (seq[i] = max(seq[i], seq[j] + 1))
    and then return max pair or sequences
"""


values = [[8, 1], [1, 2], [4, 3], [3, 4], [5, 5], [2, 6], [6, 7], [7, 8]]
# values = [[6, 2], [4, 3], [2, 6], [1, 5]]

values.sort(key=lambda x: (x[0], x[1]))
nums = [v[1] for v in values]

seq = [1 for _ in nums]
for i in range(len(nums)):
    for j in reversed(range(i)):  # 2,1,0
        if nums[j] < nums[i]:
            seq[i] = max(seq[i], seq[j] + 1)
print(max(seq))
