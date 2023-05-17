# Maximum Twin Sum of a Linked List

head = [4,2,2,3]

def pairSum(self, head: Optional[ListNode]) -> int:
    slow, fast = head, head
    maximumSum = 0

    # Get middle of the linked list.
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next

    # Reverse second half of the linked list.
    curr, prev = slow, None
    while curr:       
        curr.next, prev, curr = prev, curr, curr.next

    start = head
    while prev:
        maximumSum = max(maximumSum, start.val + prev.val)
        prev = prev.next
        start = start.next

    return maximumSum
