from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.dfs(root) != -1
    
    def dfs(self, node: Optional[TreeNode]) -> int:
        # base case
        if not node:
            return 0
        
        # if any of them is imbalanced, stop the dfs
        left_depth = self.dfs(node.left)
        if left_depth == -1:
            return -1
        right_depth = self.dfs(node.right)
        if right_depth == -1:
            return -1
        
        # if both is balanced, check if current node is balanced
        if abs(left_depth - right_depth) > 1:
            return -1
        else:
            return max(left_depth, right_depth) + 1
