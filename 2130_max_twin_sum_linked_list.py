from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next: Optional['ListNode']=None):
        self.val = val
        self.next = next
# easy approach: use stack of array to store the data
# O(1) space approach: reverse the linked list
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow, quick = head, head
        while quick:
            slow = slow.next
            quick = quick.next.next
        # now slow is at the head at second half
        curr_ptr, next_ptr = slow, slow.next
        while next_ptr:
            next_ptr.next, next_ptr, curr_ptr = curr_ptr, next_ptr.next, next_ptr
        slow.next = None

        result = 0
        while curr_ptr and head:
            result = max(result, curr_ptr.val+head.val)
            curr_ptr = curr_ptr.next
            head = head.next
        return result
            