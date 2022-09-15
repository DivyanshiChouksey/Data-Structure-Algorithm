# Find Original Array From Doubled Array

"""
    Create a counter of given array and sort it after that iterate through the sorted counter
    if current value frequency is greater than 0 then remove as much as current value frequency from the frequency of twice of current value      
    else remove half frequency from the current value frequency.
    edge cases - if the current value is "0" with an odd frequency that means array is not a doubled array
                 if the frequency of current value i greater than thr frequency of 
                 twice of that value then also the array is not a doubled array
"""
# Time Complexity = O(nlogn) || Space Complexity = O(n)

changed = [1, 3, 4, 2, 6, 8]

from typing import Counter


def findOriginalArray(changed):
    counter = Counter(changed)
    for n in sorted(counter):
        if n == 0 and counter[n] % 2 == 1:
            return []
        if counter[n] > counter[n * 2]:
            return []
        if n:
            counter[n * 2] -= counter[n]
        else:
            counter[n] //= 2

    return list(counter.elements())


# solution2

changed = [1, 3, 4, 2, 6, 8]


def findOriginalArray2(changed):
    if len(changed) % 2 == 1:
        return []
    changed.sort()
    cnt = Counter(changed)
    ans = []
    for num in changed:
        if cnt[num] == 0:
            continue
        if cnt[2 * num] == 0:
            return []
        ans += [num]
        if num == 0 and cnt[num] % 2 == 1:
            return []
        cnt[num] -= 1
        cnt[2 * num] -= 1
    return ans


print(findOriginalArray(changed))
print(findOriginalArray2(changed))
