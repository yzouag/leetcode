from typing import Optional

from sqlalchemy import null


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummyHead = ListNode()
        curr = dummyHead
        carry = 0
        while l1 != None or l2 != None or carry != 0:
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0
            curr_sum = l1_val + l2_val + carry
            carry = curr_sum // 10
            next_node = ListNode(curr_sum%10)
            curr.next = next_node
            curr = next_node
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummyHead.next
