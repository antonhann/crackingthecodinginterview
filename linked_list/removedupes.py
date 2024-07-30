from ListNode import ListNode, printList


def removeDupes(head):
    curr = head
    while curr:
        fast = curr
        while fast.next:
            if fast.next.val == curr.val:
                fast.next = fast.next.next
            else:
                fast = fast.next
        curr = curr.next

dummy = ListNode(1)
dummy.next = ListNode(2)
dummy.next.next = ListNode(3)
dummy.next.next.next = ListNode(2)

printList(dummy)

removeDupes(dummy)

printList(dummy)