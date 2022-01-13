from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def create_list(a : List):
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

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # method 1 iterative method
        # prev = None
        # while head:
        #     temp = head.next
        #     head.next = prev
        #     prev = head
        #     head = temp
        # return prev

        # method 2 recursive:
        if head is None or head.next is None: 
            return head
        node, head.next.next, head.next = self.reverseList(head.next), head, None
        return node

if __name__ == "__main__":
    list1 = create_list([2,3,4,9])
    print_list(Solution().reverseList(list1))