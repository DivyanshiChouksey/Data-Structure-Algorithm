# Merge k Sorted Lists

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

"""
    Initilaize an empty heap then push all no. of head of linkedlist in it with 3 parameter 
    cur node.val, count (no of time it occurs), and the cur node address
    then create a dummy node and a pointer initially pointing at dummy node after that do the steps 
    while heap is not empty - pop the node (ie smallest node val using minimize heap) and attach it to the next
    of current pointing node and repeat for the next node of this popped node 
    return the dummy.next ie the head of Merge k Sorted Lists. 

"""

# Time Complexity = O(nlogk) || Space Complexity = O(k)

import heapq

lists = [[1,4,5],[1,3,4],[2,6]]
# Output = [1,1,2,3,4,4,5,6]

def mergeKLists(lists):
    heap = []
    count = 0 
    for node in lists:
        if node:
            count += 1
            heapq.heappush(heap, (node.val, count, node))
    dummy = ListNode(0)
    cur = dummy
    while heap:
        _, _, tmp = heapq.heappop(heap)
        cur.next = tmp
        cur = tmp
        if tmp.next:
            count+=1
            heapq.heappush(heap, (tmp.next.val, count, tmp.next))
    
    return dummy.next


# 
# [(1, 1, ListNode{val: 1, next: ListNode{val: 4, next: ListNode{val: 5, next: None}}}), 
#  (1, 2, ListNode{val: 1, next: ListNode{val: 3, next: ListNode{val: 4, next: None}}}), 
#  (2, 3, ListNode{val: 2, next: ListNode{val: 6, next: None}})]  
