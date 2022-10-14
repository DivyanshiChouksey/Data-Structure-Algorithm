# Right Smaller Than

# Time Complexity = O(n^2) || Space Complexity = O(n)


def rightSmallerThan(array):
    ans = []
    for i in range(len(array)):
        count = 0
        for j in range(i + 1, len(array)):
            if array[j] < array[i]:
                count += 1
        ans.append(count)
    return ans
