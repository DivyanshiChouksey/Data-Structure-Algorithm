# LinkedListPalindrome

head = 1


def linkedListPalindrome(head):
    slow = head
    fast = head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

    reversedSecondHalf = reverseLinkedList(slow)
    firstHalf = head

    while reversedSecondHalf:
        if reversedSecondHalf.value != firstHalf.value:
            return False
        reversedSecondHalf = reversedSecondHalf.next
        firstHalf = firstHalf.next

    return True


def reverseLinkedList(head):
    prev = None
    current = head
    while current:
        tmp = current.next
        current.next = prev
        prev = current
        current = tmp
    return prev


print(linkedListPalindrome(head))
