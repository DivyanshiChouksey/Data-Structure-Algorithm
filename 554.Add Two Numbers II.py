# Add Two Numbers II

# Definition for singly-linked list.
class LinkedList:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

l1 = LinkedList(7)
n1 = LinkedList(2)
n2 = LinkedList(4)
n3 = LinkedList(3)

l2 = LinkedList(5)
n4 = LinkedList(6)
n5 = LinkedList(4)


l1.next = n1
n1.next = n2
n2.next = n3

l2.next = n4
n4.next = n5

# l1 = [7,2,4,3]
# l2 = [5,6,4]
# Output: [7,8,0,7]

def addTwoNumbers(l1,l2):
    
    def display(ll):
        tmp = ""
        while ll:
            tmp += str(ll.val)
            ll = ll.next
        return tmp

    ans = str(int(display(l1)) + int(display(l2)))
    head = node = LinkedList(int(ans[0]))
    i=1
    while i<len(ans):
        node.next = LinkedList(int(ans[i]))
        node = node.next
        i+=1

    return head


m = addTwoNumbers(l1,l2)
while m is not None:
    print(m.val)
    m = m.next