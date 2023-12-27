# Minimum Time to Make Rope Colorful

colors = "abaac"
neededTime = [1,2,3,4,5]


def minCost(colors,neededTime):
    ans = 0
    maxVal =0
    # for i in range(len(neededTime)):
    i=0
    j=0
    while j<len(colors) and i<len(colors):
        curTotal = 0
        curMax= 0
        while j<len(colors) and colors[i] == colors[j]:
            curTotal+=neededTime[j]
            curMax = max(curMax,neededTime[j])                
            j+=1
        ans+=(curTotal-curMax)
        i = j
    return ans


print( minCost(colors,neededTime))
