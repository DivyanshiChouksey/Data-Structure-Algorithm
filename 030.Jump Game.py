# Jump Game
"""
    greedy solution :- we keep track of jumps,steps,maximum reach we can from anystep
    so when we are out of step we add maxReach to our steps and increase jump
    when steps < 0 in that case return False
"""
# Time Complexity = O()|| Space Complexity = O()

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
