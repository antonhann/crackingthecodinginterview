class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = None

def printList(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next    
    print()