from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        if not root:
            return res
        
        queue = [root]
        direction = 0
        while queue:
            next_queue = []
            level_values = []
            for node in queue:
                if node is not None:
                    level_values.append(node.val)
                    next_queue.append(node.left)
                    next_queue.append(node.right)
            if next_queue:
                if direction == 1:
                    level_values.reverse()
                res.append(level_values)
            queue = next_queue
            direction = (direction + 1)%2
        
        return res