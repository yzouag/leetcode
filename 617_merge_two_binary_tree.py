from typing import Optional
import collections

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        # method 1: recursion
        """
        if root1 and root2: # if the node exists for both tree
            root = TreeNode(root1.val+root2.val)
            root.left = self.mergeTrees(root1.left, root2.left)
            root.right = self.mergeTrees(root1.right, root2.right)
            return root
        else: # else, return the one which is not null or simply a null
            return root1 or root2
        """
        
        # method 2: BFS
        q1 = collections.deque()
        q2 = collections.deque()
        

if __name__ == "__main__":
    pass