from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxAncestorDiff(root: Optional[TreeNode]) -> int:
        def dfs(node: TreeNode, min_val, max_val, max_diff):
            res = max([max_diff, abs(min_val-node.val), abs(max_val-node.val)])
            if node.left:
                res = dfs(node.left, min(min_val, node.val), max(max_val, node.val), res)
            if node.right:
                res = dfs(node.right, min(min_val, node.val), max(max_val, node.val), res)
            return res
        
        res = 0
        if root.left:
            res = dfs(root.left, root.val, root.val, res)
        if root.right:
            res = dfs(root.right, root.val, root.val, res)
        return res

