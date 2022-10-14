from sortedcontainers import SortedList

# 1,2,2,2,3      2

s = SortedList()
nums = [5, 2, 6, 1]
ans = []
for num in nums[::-1]:
    n = SortedList.bisect_left(s, num)  # idx #log n
    s.add(num)  # log n
    ans.append(n)  # 0,1,1,2 # constant
# return ans[::-1]
