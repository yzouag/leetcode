from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        rev = None
        while fast and fast.next:
            fast = fast.next.next
            temp = rev
            rev = slow
            slow = slow.next
            rev.next = temp
        # if the list is odd number length, slow will stop at the center
        # and center no needs to compare
        # 1 <- 2 <- 3 -> 2 -> 1
        #      r    s         f
        # we need to step slow one further
        # 1 <- 2 <- 3 -> 2 -> 1
        #      r         s    f
        if fast: 
            slow = slow.next
        while rev and rev.val == slow.val:
            rev = rev.next
            slow = slow.next
        return not rev
