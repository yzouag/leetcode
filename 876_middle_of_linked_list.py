from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# understand optional: https://stackoverflow.com/questions/51710037/how-should-i-use-the-optional-type-hint
class Solution:
    # my method: easy, but slow and O(n) in space
    # def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
    #     pointer_list = []
    #     pointer_list.append(head)
    #     while head.next != None:
    #         head = head.next
    #         pointer_list.append(head)
    #     return pointer_list[len(pointer_list)//2]
    
    # better:
    # two pointers: one slow, one fast, fast steps twice faster than slow, return slow
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow_ptr = head
        fast_ptr = head
        while fast_ptr is not None and fast_ptr.next is not None:
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next
        return slow_ptr
    
    def print_list(self, head: Optional[ListNode]):
        print('[')
        if head == None:
            print(']')
            return
        while True:
            print(head.val)
            if head.next is None:
                break
        print(']')

if __name__ == "__main__":
    a = [1,2,3,4,5]
    Solution().print_list(Solution().middleNode(a))