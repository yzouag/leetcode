from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        s1 = []
        s2 = []

        # put l1, l2 into stack
        while l1:
            s1.append(l1.val)
            l1 = l1.next
        while l2:
            s2.append(l2.val)
            l2 = l2.next

        ans = ListNode()
        carry = 0
        total_sum = 0
        while s1 or s2:
            if s1:
                total_sum += s1.pop()
            if s2:
                total_sum += s2.pop()
            if total_sum > 9:
                ans.val = total_sum % 10
                carry = 1
            else:
                ans.val = total_sum
                carry = 0
            total_sum = carry
            head = ListNode(carry, ans)
            ans = head

        return ans if carry == 1 else ans.next