# Remove Nodes From Linked List

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

# Optimize solution 
"""
simplifying the ques: the ques want us to order the linked list into decrease order by Removing every node which has a node with a greater value anywhere to the 
right side of it.

The idea is to first reverse the linked list to make so that now we need to order the linked list into increasing order as this will be easy to do.
now initialise maximum variable that will store maximuum value so far and current pointer at head and a prev pointer as None.
Iterate the linkedlist if cur.val < maximum delete the current node (by skipping it i.e prev.next = cur.next)
else move prev and cur by one pointer and at the end again reverse the modifyied linkedlist and return it.
"""
# Time Complexity = O(n) || Space Complexity = O(1)

class Solution:
    def reverse_list(self,head):
        node = head
        prev = None
        while node:
            tmp = node.next
            head.next = prev
            prev = head
            head = tmp

        return prev

    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        head = self.reverse_list(head)

        maxi = 0
        prev = None
        curr = head

        while curr:
            maxi = max(maxi,curr.val)
            if curr.val < maxi:
                prev.next = curr.next
                # deleted = curr
                curr = curr.next
            else:
                prev = curr
                curr = curr.next
                
        return self.reverse_list(head)



# Naive solution 

"""
    Creating a dummy node which is pointing to head and using stack data structure
    initially having dummy node in it then go through the linkedlist and push values into stack
    if they are strickly greater than top value of stack else just pop the 
    value until we get a greater value than current value and also keeo track of the underflow condition 
    after that return the dummy.next
"""

# Time Complexity = O(n) || Space Complexity = O(n)


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
