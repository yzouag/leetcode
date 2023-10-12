from typing import List, Optional
from collections import defaultdict
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        counts = defaultdict(int)
        maxFreq = 0
        res = []
        def dfs(root: TreeNode) -> int:
            nonlocal maxFreq
            nonlocal res
            left_sub = right_sub = 0
            if root.left:
                left_sub = dfs(root.left)
            if root.right:
                right_sub = dfs(root.right)
            current_sum = left_sub + right_sub + root.val
            counts[current_sum] += 1
            if counts[current_sum] == maxFreq:
                res.append(current_sum)
            elif counts[current_sum] > maxFreq:
                res = [current_sum]
                maxFreq = counts[current_sum]
            return current_sum
        dfs(root)
        return res