from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        dummy = curr = ListNode()
        slow, fast = head, head.next
        while slow:
            if slow.next:
                fast = slow.next
            else:
                break
            curr.next = fast
            slow.next = fast.next
            fast.next = slow
            curr = slow
            slow = slow.next

        return dummy.next