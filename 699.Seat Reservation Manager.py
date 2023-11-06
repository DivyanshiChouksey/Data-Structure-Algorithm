# Seat Reservation Manager

import heapq

# Time - O(nlogn)
# Space - O(n)
"""
Input
["SeatManager", "reserve", "reserve", "unreserve", "reserve", "reserve", "reserve", "reserve", "unreserve"]
[[5], [], [], [2], [], [], [], [], [5]]
Output
[null, 1, 2, null, 2, 3, 4, 5, null]
"""

class SeatManager:
    # time O(nlogn)
    def __init__(self, n: int):
        self.heap = [i for i in range(1,n+1)]
        heapq.heapify(self.heap)
    

    def reserve(self) -> int:
        return heapq.heappop(self.heap)
        
    def unreserve(self, seatNumber: int) -> None:
        heapq.heappush(self.heap,seatNumber)
       


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)
