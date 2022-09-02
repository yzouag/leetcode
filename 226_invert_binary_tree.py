from collections import deque
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        candidates = deque([root])
        while candidates:
            node = candidates.popleft()
            if node:
                node.left, node.right = node.right, node.left
                candidates.append(node.left)
                candidates.append(node.right)
        return root

        # recursion
        # if root:
        #     root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        # return root
        
        