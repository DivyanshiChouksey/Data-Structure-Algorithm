# Design HashSet

class MyHashSet:

    def __init__(self):
        self.ans = set()

    def add(self, key: int) -> None:
        self.ans.add(key)

    def remove(self, key: int) -> None:
        if key in self.ans:
            self.ans.remove(key)
        
    def contains(self, key: int) -> bool:
        if key in self.ans:
            return True
        return False 


# Your MyHashSet object will be instantiated and called as such:
obj = MyHashSet()
print(obj.add(1))
print(obj.add(2))
print(obj.contains(1))
print(obj.contains(3))
print(obj.add(2))
print(obj.contains(2))
print(obj.remove(2))
print(obj.contains(2))
