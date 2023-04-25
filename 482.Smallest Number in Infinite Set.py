# Smallest Number in Infinite Set

class SmallestInfiniteSet:
  def __init__(self):
      self.heap = []
      self.cur = 1
      self.seen = set()

  def popSmallest(self) -> int:
      if self.heap:
          tmp = heappop(self.heap)
          self.seen.remove(tmp)
          return tmp
      n = self.cur
      self.cur+=1
      return n

  def addBack(self, num: int) -> None:
      if num < self.cur and num not in self.seen: # 10<4
          heappush(self.heap,num)
          self.seen.add(num)

# seen - constant search
# heap [1]
# cur = 4

# 4-100
"""
Input
["SmallestInfiniteSet", "addBack", "popSmallest", "popSmallest", "popSmallest", "addBack", "popSmallest", "popSmallest", "popSmallest"]
[[], [2], [], [], [], [1], [], [], []]
Output
[null, null, 1, 2, 3, null, 1, 4, 5]
"""
