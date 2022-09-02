from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # this is a recursive solution
    # we need to keep the stack space, which is log(N)
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next: # length = 0 or 1, base case
            return head
        
        mid = self.getMid(head)
        left = self.sortList(head)
        right = self.sortList(mid)

        return self.merge(left, right)

    def getMid(self, head: ListNode) -> ListNode:
        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        mid = slow.next
        slow.next = None # break the list to two
        return mid

    def merge(self, left: ListNode, right: ListNode) -> ListNode:
        dummy = tail = ListNode()
        while left and right:
            if left.val < right.val:
                tail.next = left
                left = left.next
            else:
                tail.next = right
                right = right.next
            tail = tail.next
        tail.next = left or right # the remaining nodes
        return dummy.next