# Remove Nodes From Linked List

"""
    Creating a dummy node which is pointing to head and using stack data structure
    initially having dummy node in it then go through the linkedlist and push values into stack
    if they are strickly greater than top value of stack else just pop the 
    value until we get a greater value than current value and also keeo track of the underflow condition 
    after that return the dummy.next
"""

# Time Complexity = O(n) || Space Complexity = O(n)


class node:
    def __init__(self, val):
        self.val = val
        self.next = None


head = node(5)
n1 = node(2)
n2 = node(13)
n3 = node(3)
n4 = node(8)

head.next = n1
n1.next = n2
n2.next = n3
n3.next = n4


def removeNodes(head):
    dummy = node(float("inf"))
    dummy.next = head

    stack = [dummy]
    while head:
        while stack and stack[-1].val < head.val:
            stack.pop()
        stack[-1].next = head
        stack.append(head)
        head = head.next
    return dummy.next


m = removeNodes(head)
while m:
    print(m.val)
    m = m.next
