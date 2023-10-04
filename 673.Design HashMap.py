# Design HashMap

"""
Input
["MyHashMap", "put", "put", "get", "get", "put", "get", "remove", "get"]
[[], [1, 1], [2, 2], [1], [3], [2, 1], [2], [2], [2]]
Output
[null, null, null, 1, -1, null, 1, null, -1]
"""


class MyHashMap:

    def __init__(self):
        self.dct = {}

    def put(self, key: int, value: int) -> None:
        self.dct[key] = value

    def get(self, key: int) -> int:
        if key not in self.dct:
            return -1 
        return self.dct[key]

    def remove(self, key: int) -> None:
        if key in self.dct:
            self.dct.pop(key) 
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
