from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        k_node = head
        for _ in range(k-1):
            k_node = k_node.next

        n_k_node, end_node = head, k_node
        while end_node.next:
            n_k_node = n_k_node.next
            end_node = end_node.next
        k_node.val, n_k_node.val = n_k_node.val, k_node.val
        return head