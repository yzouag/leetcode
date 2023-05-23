from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        left = self.increasingBST(root.left)
        if left:
            tmp = left
            while tmp.right:
                tmp = tmp.right
            tmp.right = root
        root.left = None
        root.right = self.increasingBST(root.right)
        return left if left is not None else root