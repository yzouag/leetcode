from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        min_diff = 99999999
        prev_value = -1000001
        def inorder(node: Optional[TreeNode]):
            nonlocal min_diff
            nonlocal prev_value
            if not node:
                return
            inorder(node.left)
            min_diff = min(min_diff, abs(node.val-prev_value))
            prev_value = node.val
            inorder(node.right)
        inorder(root)
        return min_diff
            
