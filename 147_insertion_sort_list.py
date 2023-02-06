from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def insertionSortList(head: Optional[ListNode]) -> Optional[ListNode]:
    if not head:
        return head
    
    dummy = ListNode(-10000)
    while head:
        temp = head.next
        curr = dummy.next
        prev = dummy
        while curr is not None and curr.val <= head.val:
            prev = curr
            curr = curr.next
        prev.next = head
        head.next = curr
        head = temp
    return dummy.next