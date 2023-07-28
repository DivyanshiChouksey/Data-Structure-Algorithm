# Predict the Winner

nums = [1,5,2]

def PredictTheWinner(nums):
    n = len(nums)
    
    def maxDiff(left, right):
        if left == right:
            return nums[left]
        score_by_left = nums[left] - maxDiff(left + 1, right)
        score_by_right = nums[right] - maxDiff(left, right - 1)
        return max(score_by_left, score_by_right)
    
    return maxDiff(0, n - 1) >= 0

print(PredictTheWinner(nums))
