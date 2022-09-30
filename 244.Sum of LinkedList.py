# Sum of LinkedList

"""
    Create a new LinkedList to store the sum
    we know that number are given in reverse order so we need to store one extra variable of carry
    then we add two values from node keeping the edge case in mind that both list can be of different sizes
    for the new value it would be sum of both nodes carry and mod 10 and for carry sum of both nodes carry and
    divided by 10

"""

# Time Complexity = O(max(n,m)) ,  n-len(linkedListOne)
# Space Complexity = O(max(n,m)) ,  m - len(linkedListTwo)
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


linkedListOne = LinkedList(2)
n1 = LinkedList(6)
n2 = LinkedList(5)
n3 = LinkedList(8)

linkedListTwo = LinkedList(1)
n4 = LinkedList(3)
n5 = LinkedList(4)
n6 = LinkedList(5)

linkedListOne.next = n1
n1.next = n2
n2.next = n3

linkedListTwo.next = n4
n4.next = n5
n5.next = n6

# linkedListOne = [8,5,6,2]
# linkedListTwo = [5,4,3,1]
# sum = [1,3,9,9,3]


def sumOfLinkedLists(linkedListOne, linkedListTwo):
    newList = LinkedList(0)
    current = newList
    carry = 0

    node1 = linkedListOne
    node2 = linkedListTwo

    while node1 is not None or node2 is not None or carry != 0:
        value1 = node1.value if node1 is not None else 0
        value2 = node2.value if node2 is not None else 0
        sum = value1 + value2 + carry

        newValue = sum % 10
        node = LinkedList(newValue)
        current.next = node
        current = node

        carry = sum // 10

        node1 = node1.next if node1 is not None else None
        node2 = node2.next if node2 is not None else None

    return newList.next


newHead = sumOfLinkedLists(linkedListOne, linkedListTwo)
while newHead:
    print(newHead.value)
    newHead = newHead.next
