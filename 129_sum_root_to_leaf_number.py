from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        sums = 0
        
        def recusion(node: TreeNode, currentDigits):
            nonlocal sums
            if not node.left and not node.right:
                sums += currentDigits*10 + node.val
                return
            if node.left:
                recusion(node.left, currentDigits*10+node.val)
            if node.right:
                recusion(node.right, currentDigits*10+node.val)
        
        recusion(root, 0)
        return sums