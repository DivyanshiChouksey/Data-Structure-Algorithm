# Boats to Save People
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        # [1,1,2,2,5,7,7]
        # 7
        people.sort()
        count = 0
        l = 0
        r = len(people) - 1
        while l <= r:
            if people[r]+people[l] <= limit:
                l += 1
            r -= 1
            count += 1
        return count
