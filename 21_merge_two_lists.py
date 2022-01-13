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
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # method 1: iteratively
        # if None in (list1, list2):
        #     return list1 or list2
        # if list1 and list2:
        #     if list1.val > list2.val:
        #         head = ListNode(list2.val)
        #         list2 = list2.next
        #     else:
        #         head = ListNode(list1.val)
        #         list1  = list1.next
        #     temp = head
        #     while list1 and list2:
        #         if list1.val > list2.val:
        #             temp.next = ListNode(list2.val)
        #             list2 = list2.next
        #         else:
        #             temp.next = ListNode(list1.val)
        #             list1 = list1.next
        #         temp = temp.next
        #     temp.next = list1 or list2
        #     return head

        # method 2: recursive
        if None in (list1, list2):
            return list1 or list2
        if list1.val > list2.val:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2
        else:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1


if __name__ == "__main__":
    list1 = create_list([2,3,4,9])
    list2 = create_list([5,6,7])
    print_list(Solution().mergeTwoLists(list1, list2))