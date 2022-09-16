from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        count = 0
        def dfs(node: Optional[TreeNode], record: int):
            nonlocal count
            if node:
                record = record ^ (1 << node.val)
                if node.left == None and node.right == None: # if it's leaf node
                    if record & (record - 1) == 0:
                        # if the path is palindrome
                        # the record must be power of 2
                        # check power of 2 by x & (x-1)
                        count += 1
                else:
                    # add the current value to record
                    # use xor to add on correspond digit
                    dfs(node.left, record)
                    dfs(node.right, record)
        dfs(root, 0)
        return count