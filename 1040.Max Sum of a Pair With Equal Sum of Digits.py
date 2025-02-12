# Max Sum of a Pair With Equal Sum of Digits
class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        dct = {}
        ans =-1
        for num in nums:
            tmp = 0
            for ch in str(num):
                tmp+=int(ch)
            if tmp not in dct:
                dct[tmp] = num
            else:
                ans = max(ans,dct[tmp]+num)
                dct[tmp] = max(dct[tmp],num)
        return ans

        
        # def sum_of_digit(num):
        #     ans = 0
        #     while num:
        #         ans += num%10
        #         num = num//10 
        #         print(num)
        #     return ans


        # dct = {}
        # for i in range(len(nums)):
        #     flag = False
        #     if sum_of_digit(nums[i]) in dct:
        #         flag = True
        #         dct[sum_of_digit(nums[i])] +=nums[i]
        #     else:
        #         dct[sum_of_digit(nums[i])] = nums[i]
        # return max(dct.values()) if flag else -1

        
