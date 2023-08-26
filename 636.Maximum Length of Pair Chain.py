# Maximum Length of Pair Chain

pairs = [[1,2],[7,8],[4,5]]

def findLongestChain(pairs):
    pairs.sort(key=lambda x: x[1])
    curr = float('-inf')
    ans = 0

    for pair in pairs:
        if pair[0] > curr:
            ans += 1
            curr = pair[1]
    return ans

print(findLongestChain(pairs))
