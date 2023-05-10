from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self) -> None:
        self.res = None
    
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':        
        def dfs(root: Optional[TreeNode]):
            if not root:
                return False
            left = dfs(root.left)
            right = dfs(root.right)
            if root.val == q.val or root.val == p.val:
                center = True
            else:
                center = False
            
            if left + right + center >= 2:
                self.res = root
            return left or right or center
        dfs(root)
        return self.res