# Double a Number Represented as a Linked List

Input: head = [9,9,9]
Output: [1,9,9,8]


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse_list(self,head):
        node = head
        prev = None
        while node:
            tmp = node.next
            node.next = prev
            prev = node
            node = tmp
        return prev


    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        head = self.reverse_list(head)
        cur = head
        carry = 0

        while cur:
            newSum = (cur.val*2)+carry
            newVal = newSum%10
            cur.val = newVal
            carry = newSum//10
            if cur.next:
                cur = cur.next
            else:
                break

        if carry:
            cur.next = ListNode(carry)
        
        return self.reverse_list(head)

            
