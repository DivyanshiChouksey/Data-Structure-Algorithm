# Delete Columns to Make Sorted

strs = ["cba", "daf", "ghi"]

# Best Solution
"""
    We traverse column wise in the given Strs then keep track that our next character is lexicographically
    bigger than our previous character then update this as our current character 
    if not then we increase our count and break inner loop
"""
# Time Complexity = O(mn) || Space Complexity = O(1)


def minDeletionSize1(strs):
    cnt = 0
    for i in range(len(strs[0])):
        tmp = strs[0][i]
        for j in range(len(strs)):
            if tmp > strs[j][i]:
                cnt += 1
                break
            tmp = strs[j][i]
    return cnt


# Effective Solution
"""
    Instead of making another transpose Strs we keep track of coloumn elements only 
    go through the given Strs and store the coloumn elements in tmp and increase count if sorted tmp is not equals 
    to current tmp list and return the ans 
"""
# Time Complexity = O(nm log(m)) || Space Complexity = O(m)


def minDeletionSize2(strs):
    cnt = 0
    for i in range(len(strs[0])):
        tmp = ""
        for j in range(len(strs)):
            tmp += strs[j][i]
        cnt += sorted(tmp) != list(tmp)

    return cnt


# Naive Solution
"""
    To get access of element in coloumn wise manner we transpose the given Strs then
    an ans to store the count and after that go throught the strs and if list of coloumn elements is not
    equal to sorted coloumn element then increase ans by one at the end return the ans 
"""
# Time Complexity = O(nm log(m)) || Space Complexity = O(mn)


def minDeletionSize3(strs):
    strs[::] = zip(*strs)
    ans = 0
    for col in strs:
        if list(col) != sorted(col):
            ans += 1

    return ans


print(minDeletionSize1(strs))
print(minDeletionSize2(strs))
print(minDeletionSize3(strs))
