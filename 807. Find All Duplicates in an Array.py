#  Find All Duplicates in an Array

nums = [4,3,2,7,8,2,3,1]

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        array = []
        for n in nums:
            if nums[abs(n)-1]<0:
                array.append(abs(n))
            else:
                nums[abs(n)-1]*=-1

        return array
