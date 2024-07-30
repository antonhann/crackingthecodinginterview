from ListNode import ListNode, printList

def kthLast(head, k):
    runner = head
    for i in range(k):
        if runner:
            runner = runner.next
    curr = head
    while runner:
        runner = runner.next
        curr = curr.next    
    return curr

dummy = ListNode(1)
dummy.next = ListNode(2)
dummy.next.next = ListNode(3)
dummy.next.next.next = ListNode(2)
val = 4
print(kthLast(dummy,val).val if kthLast(dummy,val) else None)