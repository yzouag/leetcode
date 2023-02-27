from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        min_diff = 999999
        prev = -1
        def inorder_traversal(node: TreeNode): # for BST, inorder will be increasing order
            nonlocal prev
            nonlocal min_diff
            if not node:
                return
            inorder_traversal(node.left)
            if prev != -1:
                min_diff = min(min_diff, abs(prev-node.val))
            prev = node.val
            inorder_traversal(node.right)
        inorder_traversal(root)
        return min_diff
