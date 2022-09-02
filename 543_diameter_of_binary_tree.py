from typing import Optional, Tuple
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        return self.dfs(root)[1]-1
    
    def dfs(self, node: Optional[TreeNode]) -> Tuple[int, int]:
        if not node:
            return (0, 0)
        depth_l, diameter_l = self.dfs(node.left)
        depth_r, diameter_r = self.dfs(node.right)
        
        diameter_current = depth_l + depth_r + 1
        depth_current = max(depth_l, depth_r) + 1
        return depth_current, max([diameter_l, diameter_current, diameter_r])