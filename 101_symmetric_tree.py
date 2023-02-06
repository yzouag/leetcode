from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isSymmetric(root: Optional[TreeNode]) -> bool:
    if not root:
        return True
    
    def checkSymmetry(left: Optional[TreeNode], right: Optional[TreeNode]) -> bool:
        if not left and not right:
            return True
        if (left and not right) or (right and not left) or (left.val != right.val):
            return False
        return checkSymmetry(left.left, right.right) and checkSymmetry(left.right, right.left)
    
    return checkSymmetry(root.left, root.right)