# LinkedListPalindrome

"""
    For a valid palindrome linkedList we have to follow some basic and essential steps:
        1. do the half partition of given linkedlist by slow and fast pointer method(floyd cycle detection method)
        2. after that reversed the second half of the linked list
        3. then check firstHalf node value one by one by comparing with secondhalf node value respectively
        4. return true if firsthalf is equal to secondhalf else false.
"""
# Time Complexity = O(n) || Space Complexity = O(1)


class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


head = LinkedList(0)
n1 = LinkedList(1)
n2 = LinkedList(2)
n3 = LinkedList(2)
n4 = LinkedList(1)
n5 = LinkedList(0)

head.next = n1
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5


def linkedListPalindrome(head):
    slow = head
    fast = head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

    reversedSecondHalf = reverseLinkedList(slow)
    firstHalf = head

    while reversedSecondHalf:
        if reversedSecondHalf.value != firstHalf.value:
            return False
        reversedSecondHalf = reversedSecondHalf.next
        firstHalf = firstHalf.next

    return True


def reverseLinkedList(head):
    prev = None
    current = head
    while current:
        tmp = current.next
        current.next = prev
        prev = current
        current = tmp
    return prev


print(linkedListPalindrome(head))
