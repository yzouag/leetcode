from typing import List, Optional
import heapq

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # method 1: heap
        # use heap to compare all columns in O(logK) time, K is the number of array
        # head = ListNode() # dummy node
        # current = head
        # next_min_pool = []
        # for i, node in enumerate(lists):
        #     if node:
        #         heapq.heappush(next_min_pool, (node.val, i, node))
        # while len(next_min_pool) > 0:
        #     next_val, i, next_node = heapq.heappop(next_min_pool)
        #     current.next = ListNode(next_val)
        #     current = current.next
        #     if next_node.next:
        #         next_node = next_node.next
        #         heapq.heappush(next_min_pool, (next_node.val, i, next_node))
        # return head.next

        # method 2: merge with divide and conquer
        # merge two list, each in length N/k, this requires O(N) computation
        # then merge the merged list which is 2N/k .... all with O(N) computation
        # in total logk layer, thus the total compuatation is O(Nlogk)
        def mergeTwoList(l1 : Optional[ListNode], l2 : Optional[ListNode]) -> Optional[ListNode]:
            head = current = ListNode()
            while l1 and l2:
                if l1.val > l2.val:
                    current.next = l2
                    l2 = l2.next
                else:
                    current.next = l1
                    l1 = l1.next
                current = current.next
            if l1:
                current.next = l1
            else:
                current.next = l2
            return head.next
        
        # how to implement merge is the most tricky part!!!
        interval = 1
        amount = len(lists)
        while interval < amount:
            for i in range(0, amount-interval, interval*2):
                lists[i] = mergeTwoList(lists[i], lists[i+interval])
            interval *= 2
        return lists[0] if amount > 0 else None

def printListNode(head : ListNode) -> List[int]:
    s = []
    while head != None:
        s.append(head.val)
        head = head.next
    return s

if __name__ == "__main__":
    pass