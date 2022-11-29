# Insert Delete GetRandom O(1)

"""
    Create a set to keep record of values also to get their access in constant time,
    1. for insert check is that value is in the set if yes then return False else add the 
        value in the set and return True.
    2. for remove check is that value is in the set if yes then remove the value from the set and return True
        else return False.
    3. and lastly for getRandom using in-built function random(random.sample(self.r, 1)[0]) to return the random value.
"""

# Time Complexity = O(1) || Space Complexity = O(n)


import random


class RandomizedSet:
    def __init__(self):
        self.r = set()

    def insert(self, val: int) -> bool:
        if val in self.r:
            return False
        self.r.add(val)
        return True

    def remove(self, val: int) -> bool:
        if val in self.r:
            self.r.remove(val)
            return True
        return False

    def getRandom(self) -> int:
        return random.sample(self.r, 1)[0]


obj = RandomizedSet()
print(obj.insert(1))
print(obj.remove(2))
print(obj.getRandom())
print(obj.insert(2))
print(obj.remove(2))
print(obj.getRandom())
