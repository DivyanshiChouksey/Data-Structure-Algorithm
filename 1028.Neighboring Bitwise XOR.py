# Neighboring Bitwise XOR

class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        XOR = 0
        for element in derived:
            XOR = XOR ^ element
        return XOR == 0


class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        return sum(derived) % 2 == 0
