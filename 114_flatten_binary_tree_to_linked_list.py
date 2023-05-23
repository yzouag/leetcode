from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        
        def traverse(node: Optional[TreeNode]):
            if not node:
                return None
            right_child = node.right
            node.right = traverse(node.left)
            node.left = None
            temp = node
            while temp.right:
                temp = temp.right
            temp.right = traverse(right_child)
            return node

        traverse(root)