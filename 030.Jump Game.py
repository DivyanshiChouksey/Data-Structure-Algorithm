# Jump Game
"""
    Greedy solution 
    We start from the back of array and then 
    keep the track of maximum distance we can go from that index 
    if (i+nums[i]) >= goal then update goal to i
    and if our goal is zero that means we cannot go after that point so return False.
    
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
