# coin change
# coin change II
# jump game
# jump game II


coins = [1, 2, 5]
amount = 11


def coinChange(coins, amount):
    dp = [float("inf") for i in range(amount + 1)]
    dp[0] = 0
    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)
    if dp[-1] == float("inf"):
        return -1
    return dp[-1]


print(coinChange(coins, amount))

# ----------------------------------------------------------------------------


amount = 5
coins = [1, 2, 5]


def change(amount, coins):
    dp = [0 for i in range(amount + 1)]
    dp[0] = 1
    for coin in coins:
        for i in range(coin, len(dp)):
            dp[i] += dp[i - coin]

    return dp[-1]


print(change(amount, coins))


# ------------------------------------------------------------------------

nums = [2, 3, 1, 1, 4]


def jumpGame(nums):
    goal = len(nums) - 1

    for i in range(len(nums) - 1, -1, -1):
        if i + nums[i] >= goal:
            goal = i
    if goal == 0:
        return True
    else:
        return False


print(jumpGame(nums))

# --------------------------------------------------------------------------


# water Area

height = [0, 8, 0, 0, 5, 0, 0, 10, 0, 0, 1, 1, 0, 3]


# def waterArea(height):
maxes = [0 for i in range(len(height))]
print(maxes)

leftMax = 0
for i in range(len(height)):
    maxes[i] = leftMax
    leftMax = max(leftMax, height[i])
# print(maxes)
rightMax = 0
for i in range(len(height) - 1, -1, -1):
    minHeight = min(maxes[i], rightMax)
    if height[i] <= minHeight:
        maxes[i] = minHeight - height[i]
    else:
        maxes[i] = 0
    rightMax = max(rightMax, height[i])

# print(maxes)
print(sum(maxes))


# -------------------------------------------------------------------------

# edit distance *************


str1 = "horse"
str2 = "ros"

# def editDistance(str1,str2):
dp = [[0 for i in range(len(str1) + 1)] for j in range(len(str2) + 1)]
# print(dp)
for i in range(len(str1) + 1):
    dp[0][i] = i
for j in range(len(str2) + 1):
    dp[j][0] = j

for i in range(1, len(str1) + 1):
    for j in range(1, len(str2) + 1):
        if str1[i - 1] == str2[j - 1]:
            dp[i][j] = dp[i - 1][j - 1]
        else:
            print(i, j, dp[i - 1][j - 1])
            dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1

print(dp)

# ---------------------------------------------------------------------------------
