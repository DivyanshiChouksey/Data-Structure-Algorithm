class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


# head = LinkedList(0)
# n1 = LinkedList(1)
# n2 = LinkedList(2)
# n3 = LinkedList(3)
# n4 = LinkedList(4)
# n5 = LinkedList(5)
# n6 = LinkedList(6)


# head.next = n1
# n1.next = n2
# n2.next = n3
# n3.next = n4
# n4.next = n5
# n5.next = n6
# n6.next = n3

## 1. Reverse a LinkedList
# def reverseLinkedList(head):
#     prev = None
#     while head:
#         tmp = head.next
#         head.next = prev
#         prev = head
#         head = tmp

#     return prev


# newHead = reverseLinkedList(head)
# while newHead:
#     print(newHead.value)
#     newHead = newHead.next

# --------------------------------------------------------

## 2. Remove Duplicate
# def removeDuplicates(head):
#     node = head
#     while node:
#         dNode = node.next
#         while dNode and dNode.value == node.value:
#             dNode = dNode.next
#         node.next = dNode
#         node = dNode
#     return head


# newHead = removeDuplicates(head)
# while newHead:
#     print(newHead.value)
#     newHead = newHead.next

# ------------------------------------------------------------

## 3. Remove Kth Node From End Of LinkedList
# k = 2


# def removeKthNodeFromEnd(head, k):
#     count = 1
#     first = head
#     second = head
#     while count <= k:
#         second = second.next
#         count += 1

#     if second is None:
#         return head.next

#     while second.next:
#         second = second.next
#         first = first.next
#     first.next = first.next.next
#     return head


# newHead = removeKthNodeFromEnd(head, k)
# while newHead:
#     print(newHead.value)
#     newHead = newHead.next

# ----------------------------------------------------------

## 4. Find Loop
# def findLoop(head):
#     slow = head.next
#     fast = head.next.next
#     while fast != slow:
#         slow = slow.next
#         fast = fast.next.next

#     slow = head
#     while fast != slow:
#         slow = slow.next
#         fast = fast.next

#     return slow.value
# print(findLoop(head))

# --------------------------------------------------------------

# ## 5. Merge Linked Lists

# head = LinkedList(0)
# n1 = LinkedList(2)
# n2 = LinkedList(3)
# n3 = LinkedList(5)

# head2 = LinkedList(1)
# n4 = LinkedList(2)
# n5 = LinkedList(4)
# n6 = LinkedList(6)
# n7 = LinkedList(9)
# n8 = LinkedList(10)

# head.next = n1
# n1.next = n2
# n2.next = n3

# head2.next = n4
# n4.next = n5
# n5.next = n6
# n6.next = n7
# n7.next = n8


# def mergeLinkedLists(head, head2):
#     prev = None
#     p1 = head
#     p2 = head2

#     while p1 is not None and p2 is not None:
#         if p1.value < p2.value:
#             prev = p1
#             p1 = p1.next
#         else:
#             if prev is not None:
#                 prev.next = p2
#             prev = p2
#             p2 = p2.next
#             prev.next = p1

#     if p1 is None:
#         prev.next = p2

#     return head if head.value < head2.value else head2


# newHead = mergeLinkedLists(head, head2)
# while newHead:
#     print(newHead.value)
#     newHead = newHead.next

# ----------------------------------------------------------------------

## 6. Sum Of LinkedList
# head = LinkedList(2)
# n1 = LinkedList(6)
# n2 = LinkedList(5)
# n3 = LinkedList(8)

# head2 = LinkedList(1)
# n4 = LinkedList(3)
# n5 = LinkedList(4)
# n6 = LinkedList(5)

# head.next = n1
# n1.next = n2
# n2.next = n3

# head2.next = n4
# n4.next = n5
# n5.next = n6


# def sumOfLinkedLists(head, head2):
#     newlist = LinkedList(0)
#     current = newlist
#     carry = 0
#     node1 = head
#     node2 = head2

#     while node1 is not None or node2 is not None or carry != 0:
#         value1 = node1.value if node1 else 0
#         value2 = node2.value if node2 else 0
#         sum = value1 + value2 + carry

#         newValue = sum % 10
#         newnode = LinkedList(newValue)
#         current.next = newnode
#         current = newnode

#         carry = sum // 10

#         node1 = node1.next if node1 else None
#         node2 = node2.next if node2 else None

#     return newlist.next


# newHead = sumOfLinkedLists(head, head2)
# while newHead:
#     print(newHead.value)
#     newHead = newHead.next
