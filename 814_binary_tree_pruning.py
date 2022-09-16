from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def pruned(node: Optional[TreeNode]) -> bool:
            if not node:
                return True
            if pruned(node.left):
                node.left = None
            if pruned(node.right):
                node.right = None
            if node.left == None and node.right == None and node.val == 0:
                return True
            return False
        if pruned(root):
            return None
        return root