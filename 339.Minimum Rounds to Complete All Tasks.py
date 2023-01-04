# Minimum Rounds to Complete All Tasks

"""
    Create a counter of tasks and then check if value is 1 then return -1 as only 1 is not able to obtain by 2 and 3
    otherwise check if value is divisible by 3 then increase the count of round and is not divisible then count by 
    div+1 and return the count
"""

# Time Complexity = O(n) || Space Complexity = O(n)

tasks = [2, 2, 3, 3, 2, 4, 4, 4, 4, 4]

from collections import Counter


def minimumRounds(tasks):
    freq = Counter(tasks)
    count = 0
    for k, v in freq.items():
        if v == 1:
            return -1
        rem = v % 3
        div = v // 3
        if rem == 0:
            count += div
        else:
            count += div + 1
    return count


print(minimumRounds(tasks))
