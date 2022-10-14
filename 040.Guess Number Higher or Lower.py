# Guess Number Higher or Lower


def guess(n):
    pass


num = 10
pick = 6
l = 0
r = num
while l <= r:
    mid = (l + r) // 2
    temp = guess(mid)
    if temp == 0:
        print(mid)
    if temp == 1:
        l = mid + 1
    else:
        r = mid - 1
