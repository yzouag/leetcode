from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isSameTree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    if not p and not q:
        return True
    if (p and not q) or (q and not p) or (p.val != q.val):
        return False
    return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)