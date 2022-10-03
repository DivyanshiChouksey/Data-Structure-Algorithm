# Sum of Linked Lists

"""
    Create a new LinkedList to store the sum
    we know that number are given in reverse order so we need to store one extra variable of carry
    then we add two values from node keeping the edge case in mind that both list can be of different sizes
    for the new value it would be sum of both nodes carry and mod 10 and for carry sum of both nodes carry and
    divided by 10.
"""

# Time Complexity = O(max(n,m))   , n = len of 1st linkedlist
# Space Complexity = O(max(n,m))  , m = len of 2nd linkedlist


class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


linkedListOne = LinkedList(2)
n1 = LinkedList(4)
n2 = LinkedList(7)
n3 = LinkedList(1)

linkedListTwo = LinkedList(9)
n5 = LinkedList(4)
n6 = LinkedList(5)

linkedListOne.next = n1
n1.next = n2
n2.next = n3

linkedListTwo.next = n5
n5.next = n6


def linkedList(linkedListOne, linkedListTwo):
    newList = LinkedList(0)
    current = newList
    carry = 0

    while linkedListOne is not None or linkedListTwo is not None or carry != 0:
        value1 = linkedListOne.value if linkedListOne else 0
        value2 = linkedListTwo.value if linkedListTwo else 0
        sum = value1 + value2 + carry

        newValue = sum % 10
        node = LinkedList(newValue)
        current.next = node
        current = node

        carry = sum // 10

        linkedListOne = linkedListOne.next if linkedListOne else None
        linkedListTwo = linkedListTwo.next if linkedListTwo else None

    return newList.next


newHead = linkedList(linkedListOne, linkedListTwo)
while newHead:
    print(newHead.value)
    newHead = newHead.next
