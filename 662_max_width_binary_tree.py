from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        queue = [(root,0)]
        max_width = 0
        while queue:
            temp = []
            for node, pos in queue:
                if node.left:
                    temp.append((node.left, pos*2))
                if node.right:
                    temp.append((node.right, pos*2+1))
            max_width = max(max_width, queue[-1][1]-queue[0][1]+1)
            queue = temp
        return max_width