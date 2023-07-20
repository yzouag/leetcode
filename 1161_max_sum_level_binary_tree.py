from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        layer = 1
        stack = [root]
        max_sum = float('-inf')
        while stack:
            curr_sum = 0
            temp = []
            for node in stack:
                curr_sum += node.val
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            if curr_sum > max_sum:
                result = layer
                max_sum = curr_sum
            stack = temp
            layer += 1
        return result
