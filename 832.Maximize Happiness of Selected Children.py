# Maximize Happiness of Selected Children

happiness = [7,9,8,12,10]
# output = 28

class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        heap = []
        for i in range(len(happiness)):
            heapq.heappush(heap,-happiness[i])

        # print(heap)
        minus = 0
        ans= 0
        while k:
            val = -(heapq.heappop(heap))
            if val - minus > 0:
                ans+= (val-minus)
                minus+=1
                k-=1
            else:
                break

        return ans
