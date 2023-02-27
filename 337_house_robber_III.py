from typing import Optional, Tuple

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        
        def subrob(node: Optional[TreeNode]) -> Tuple[int, int]:
            # return: robCurrent, notRobCurrent
            if not node:
                return 0, 0
            
            left = subrob(node.left)
            right = subrob(node.right)

            robCurrent = node.val + left[1] + right[1] # current is robbed, only consider cases when current.left, right not robbed
            notRobCurrent = max(left) + max(right) # current is not robed, the subtree can be what ever it want
            return robCurrent, notRobCurrent
        
        return max(subrob(root))
