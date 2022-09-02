from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = jump = ListNode(0)
        dummy.next = l = r = head
        
        while True:
            count = 0
            while r and count < k:   # use r to locate the range
                r = r.next
                count += 1
            if count == k:  # if size k satisfied, reverse the inner linked list
                # now left is the head of this k, right is the head of next k
                pre, cur = r, l
                for _ in range(k):
                    temp = cur.next
                    cur.next = pre
                    pre = cur
                    cur = temp
                jump.next = pre # link this group tail with next group head
                jump = l # jump should be the tail of this group
                l = r
            else:
                return dummy.next
