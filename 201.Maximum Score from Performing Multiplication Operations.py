# Maximum Score from Performing Multiplication Operations

nums = [1,2,3]
multipliers = [3,2,1]

def maximumScore(self, nums, multipliers) -> int:
        m = len(multipliers)
        n = len(nums)
        dp = [0] * (m + 1)
        for op in range(m - 1, -1, -1):
            next_row = dp.copy()
            # Present Row is now next_Row because we are moving upwards
            for left in range(op, -1, -1):
                dp[left] = max(multipliers[op] * nums[left] + next_row[left + 1],
                               multipliers[op] * nums[n - 1 - (op - left)] + next_row[left])
        return dp[0]
        
        
#         # Number of Operations
#         m = len(multipliers)
#         # For Right Pointer
#         n = len(nums)
#         dp = [[0] * (m + 1) for _ in range(m + 1)]
        
#         for op in range(m - 1, -1, -1):
#             for left in range(op, -1, -1):
#                 dp[op][left] = max(multipliers[op] * nums[left] + dp[op + 1][left + 1],
#                                    multipliers[op] * nums[n - 1 - (op - left)] + dp[op + 1][left])
#         return dp[0][0]
        
        
#         m = len(multipliers)
        
#         def helper(left,right,i):
#             if i==m:
#                 return 0
#             return max(nums[left] * multipliers[i]+helper(left+1,right,i+1),nums[right] * multipliers[i]+helper(left,right-1,i+1))
            
#         return helper(0,len(nums)-1,0)