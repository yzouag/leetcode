# Definition for singly-linked list.
from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        sentinel = ListNode(0, head) ### best part! The sentinel!
        pred = sentinel

        while head:
            if head.next and head.val == head.next.val: # if duplicate
                while head.next and head.val == head.next.val: # traverse all duplicated and point to the last duplicate
                    head = head.next
                pred.next = head.next # let previous point to the next of the last duplicate
            else:
                pred = pred.next # not duplicate, the pred just move to the next (since next is not duplicated)

            head = head.next
        return sentinel.next

            

def create_list(a: List):
    if len(a) == 0:
        return None
    
    head = ListNode(a[0])
    temp = head
    for i in range(1,len(a)):
        temp.next = ListNode(a[i])
        temp = temp.next
    return head

def print_list(list: Optional[ListNode]):
    print('[', end='')
    while list:
        if list.next:
            print(list.val, end=', ')
        else:
            print(list.val, end='')
        list = list.next
    print(']')

if __name__ == "__main__":
    head = create_list([1,2,3,3,4,4,5])
    res = Solution().deleteDuplicates(head)
    print_list(res)

    head = create_list([1,1,1,2,3])
    res = Solution().deleteDuplicates(head)
    print_list(res)