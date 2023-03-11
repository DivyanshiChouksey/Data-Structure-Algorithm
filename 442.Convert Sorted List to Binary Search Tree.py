# Convert Sorted List to Binary Search Tree

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


"""
    Travse the linkedlist and store the node values in an array then to construct 
    the binary search tree and also it should be the height balance tree 
    find the mid of array and make treenode of that mid value then for node left 
    do this recursively in mid's left partition and for node right recursively do in mid's 
    right partition ( the way we do binary search ) 
    return node

"""

# Time Complexity = O(n) || Space Complexity = O(n) 
    
def sortedListToBST(head :ListNode):   
    arr = []
    while head:
        arr.append(head.val)
        head = head.next
    
    def helper(l,r):
        if l>r:
            return None
        m = (l+r)//2
        node =TreeNode(arr[m])
        node.left = helper(l,m-1)
        node.right = helper(m+1,r)
        return node

    return helper(0,len(arr)-1)


"""
    Approach is same as above find the mid and make it a treenode and for that node left call recursively in
    mid's left partition and for node right call recursively mid'right partition but for optimization instead of 
    traversing the linkedlist and storing the value we will traverse linkedlist by fast and slow method to get the 
    middle value the make it treenode and then update middle value as None then then for node left call recursively 
    the head and for node right call recursively the slow.next 
    return the node.
"""

# Time Complexity = O(n) || Space Complexity = O(n)
head = [-10,-3,0,5,9]


def sortedListToBST2(head : ListNode):
    if not head :
        return None
    if not head.next:
        return TreeNode(head.val)
    prev = None
    s,f = head,head
    while f and f.next:
        prev = s
        f = f.next.next
        s = s.next
    if prev:
        prev.next = None
    root = TreeNode(s.val)
    head2 = s.next
    root.left = sortedListToBST(head)
    root.right = sortedListToBST(head2)
    return root
    



print(sortedListToBST(head))
print(sortedListToBST2(head))