# Daily Temperatures

# Time : O(n)
# Space : O(n)

temperatures = [73,74,75,71,69,72,76,73]

def dailyTemperatures(temp):
    stack = []
    ans = [0]*len(temp)
    i = 0
    while i<len(temp):
        while stack and temp[stack[-1]]<temp[i]:
            j=stack.pop()
            ans[j] =  i-j
        stack.append(i)
        i+=1

    return ans


print(dailyTemperatures(temp))
