# Merge Linked List

"""
    We start by taking 3 pointers name as prev,head1,head2 
    pointing previous node initially None , head node of 1st linkedlist , head node of 2nd linkedlist respectively
    check if head1 value is smaller than head2 value then update prev as head1 value ,update next of head1 as head1 and
    prev's next will become head2 and vice versa if head2 value is smaller than head1 value 
    after that if head1 is None then prev.next = head2.
"""

# Time Complexity = O(n+m), n = length of 1st linkedlist, m = length of 2nd linkedlist
# Space Complexity = O(1)


class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


headOne = LinkedList(2)
n1 = LinkedList(6)
n2 = LinkedList(7)
n3 = LinkedList(8)

headTwo = LinkedList(1)
n4 = LinkedList(3)
n5 = LinkedList(4)
n6 = LinkedList(5)
n7 = LinkedList(9)
n8 = LinkedList(10)

headOne.next = n1
n1.next = n2
n2.next = n3

headTwo.next = n4
n4.next = n5
n5.next = n6
n6.next = n7
n7.next = n8


def mergeLinkedLists(headOne, headTwo):
    p1 = headOne
    p1prev = None
    p2 = headTwo
    while p1 is not None and p2 is not None:
        if p1.value < p2.value:
            p1prev = p1
            p1 = p1.next
        else:
            if p1prev is not None:
                p1prev.next = p2
            p1prev = p2
            p2 = p2.next
            p1prev.next = p1
    if p1 is None:
        p1prev.next = p2
    return headOne if headOne.value < headTwo.value else headTwo


newHead = mergeLinkedLists(headOne, headTwo)

while newHead:
    print(newHead.value)
    newHead = newHead.next
