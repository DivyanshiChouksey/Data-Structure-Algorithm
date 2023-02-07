# Remove Zero Sum Consecutive Nodes from Linked List

from collections import defaultdict

class LinkedList:
    def __init__(self, val):
        self.val = val
        self.next = None

head = LinkedList(1)
n1 = LinkedList(2)
n2 = LinkedList(3)
n3 = LinkedList(-3)
n4 = LinkedList(4)

head.next = n1
n1.next = n2
n2.next = n3
n3.next = n4

"""
    Scan from the left, and calculate the prefix sum whenever meet the seen prefix, 
    remove all elements of thee subarray between them.

    Steps :-
        1.Iterate the linkedlist for the first time, calulate the prefix sum and store it in hashmap 
            (like - dct[prefix_sum] = node)
        2.Iterate for the second time, check the running sum is in hashmap 
          then link it to with their next node (that means we are skipping the nodes)
            (like this :-  node.next = dct[runningSum].next)

"""

"""
    head = [1,2,3,-3,4]
    Output: [1,2,4]
"""

# Time Complexity = O(n) || Space Complexity = O(n)


def removeZeroSumSublists(head):
    dct = defaultdict()
    dummy = LinkedList(0)
    dummy.next = head
    dct[0] = dummy
    node = head
    runningSum=0
    while node:
        runningSum += node.val
        dct[runningSum] = node
        node = node.next
    
    node = dummy
    runningSum = 0
    while node:
        runningSum+=node.val
        node.next = dct[runningSum].next
        node = node.next

    return dummy.next


removeZeroSumSublists(head)
while head:
    print(head.val)
    head = head.next