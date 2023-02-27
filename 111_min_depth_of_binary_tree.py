from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        stack = [root]
        step = 1
        
        while stack:
            temp = []
            for node in stack:
                if not node.left and not node.right: # a leaf node
                    return step
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            step += 1
            stack = temp