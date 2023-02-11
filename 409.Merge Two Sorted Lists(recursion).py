# Merge Two Sorted Lists

# Time Complexity = O(n+m), n = length of 1st linkedlist,
# Space Complexity = O(n+m),  m = length of 2nd linkedlist


class LinkedList:
    def __init__(self, val):
        self.val = val
        self.next = None


list1 = LinkedList(2)
n1 = LinkedList(6)
n2 = LinkedList(7)
n3 = LinkedList(8)

list2 = LinkedList(1)
n4 = LinkedList(3)
n5 = LinkedList(4)
n6 = LinkedList(5)
n7 = LinkedList(9)
n8 = LinkedList(10)

list1.next = n1
n1.next = n2
n2.next = n3

list2.next = n4
n4.next = n5
n5.next = n6
n6.next = n7
n7.next = n8

def mergeTwoLists(list1, list2):    
    if list1 is None:
        return list2
    if list2 is None:
        return list1
    
    if list1.val < list2.val:
        list1.next = mergeTwoLists(list1.next,list2) 
        return list1  
    else:
        list2.next = mergeTwoLists(list1,list2.next)
        return list2

node = mergeTwoLists(list1, list2)

while node:
    print(node.val)
    node = node.next