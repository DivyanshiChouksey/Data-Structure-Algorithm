# Find the Winner of an Array Game

arr = [2,1,3,5,4,6,7]
k = 2

# Optimized

# Time - O(n)
# Space - O(1)

def getWinner(arr, k):
    maxEle = max(arr)
    cur = arr[0]
    count = 0
    for i in range(1,len(arr)):
        if cur> arr[i]:
            count+=1
        else:
            cur = arr[i]
            count=1
        if count == k  or cur == maxEle:
            return cur

print(getWinner(arr, k))

# Solution 2
def getWinner(arr, k):
    max_element = max(arr)
    queue = deque(arr[1:])
    curr = arr[0]
    winstreak = 0

    while queue:
        opponent = queue.popleft()
        if curr > opponent:
            queue.append(opponent)
            winstreak += 1
        else:
            queue.append(curr)
            curr = opponent
            winstreak = 1
        
        if winstreak == k or curr == max_element:
            return curr


# This would give TLE
def getWinner(arr, k):     
    count = 0
    winner = arr[0]
    queue = deque(arr)
    while True:
        a = queue.popleft()
        b = queue.popleft()
        x,y = max(a,b),min(a,b)
        queue.appendleft(x)
        queue.append(y)
        if x==winner:
            count+=1
        else:
            count = 1
            winner = x
        if count == k or winner == max(arr):
            return winner



