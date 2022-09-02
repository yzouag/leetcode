from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # length = 0, 1, 2 => no operation needed
        if head == None or head.next == None or head.next.next == None:
            return head
        even_head = head.next
        odd = head
        even = head.next
        while even and even.next:
            odd.next = even.next
            odd = even.next
            even.next = odd.next
            even = odd.next
        odd.next = even_head
        return head
        