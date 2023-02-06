from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def deleteDuplicates(head: Optional[ListNode]) -> Optional[ListNode]:
    if not head:
        return head
    
    l = r = head
    
    while r != None:
        r = r.next
        while r != None and l.val == r.val:
            r = r.next
        l.next = r
        l = r
    return head