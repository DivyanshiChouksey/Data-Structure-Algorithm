# Zip Linked List


from re import L


class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


head = LinkedList(0)
n1 = LinkedList(1)
n2 = LinkedList(2)
n3 = LinkedList(3)
n4 = LinkedList(4)
n5 = LinkedList(5)
n6 = LinkedList(6)


head.next = n1
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = n6


def zipLinkedList(linkedList):
    if linkedList.next is None or linkedList.next.next is None:
        return linkedList

    firstHalf = linkedList
    secondHalf = splitLinkedList(linkedList)
    reversedSecondHalfHead = reverseLinkedList(secondHalf)
    return interweaveLinkedList(firstHalf, reversedSecondHalfHead)


def splitLinkedList(linkedList):
    slow = linkedList
    fast = linkedList
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

    secondHalf = slow.next
    slow.next = None
    return secondHalf


def interweaveLinkedList(linkedList1, linkedList2):
    list1 = linkedList1
    list2 = linkedList2
    while list1 is not None and list2 is not None:
        tmp1 = list1.next
        tmp2 = list2.next

        list1.next = list2
        list2.next = tmp1

        list1 = tmp1
        list2 = tmp2
    return linkedList1


def reverseLinkedList(linkedList):
    prev = None
    current = linkedList
    while current:
        tmp = current.next
        current.next = prev
        prev = current
        current = tmp
    return prev


m = zipLinkedList(head)
while m:
    print(m.value)
    m = m.next
