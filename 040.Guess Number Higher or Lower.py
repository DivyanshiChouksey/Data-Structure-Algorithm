# Guess Number Higher or Lower


def guess(n):
    pass


# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

"""
    use binary Search
"""

# Time Complexity = O(logn) || Space Complexity = O(1)


def guessNumber(n):
    l = 0
    r = n
    while l <= r:
        mid = l + (r - l) // 2
        tmp = guess(mid)
        if tmp == 0:
            return mid
        elif tmp == 1:
            l = mid + 1
        else:
            r = mid - 1


"""
    by using for loop check for each number in range of n
    (might occur Time Limit Exceeds)
"""

# Time Complexity = O(n) || Space Complexity = O(1)


def guessNumber(n):
    for i in range(n + 1):
        if guess(i) == 0:
            return i
