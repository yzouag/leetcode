from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        # method 1: convert to string for compare
        # def convert(s: TreeNode):
        #     return '^' + s.val + convert(s.left) + convert(s.right) if s else '#'
        # return convert(subRoot) in convert(root)

        # method 2: merkle hash
        from hashlib import sha256
        def hash_(x):
            S = sha256()
            S.update(x)
            return S.hexdigest()
            
        def merkle(node):
            if not node:
                return '#'
            m_left = merkle(node.left)
            m_right = merkle(node.right)
            node.merkle = hash_(m_left + str(node.val) + m_right)
            return node.merkle
            
        merkle(root)
        merkle(subRoot)
        
        def dfs(node):
            if not node:
                return False
            return (node.merkle == subRoot.merkle or dfs(node.left) or dfs(node.right))
                        
        return dfs(root)