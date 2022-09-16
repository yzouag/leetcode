from collections import defaultdict
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.ans = 0
        cache = defaultdict(int)
        cache[0] = 1
        
        def dfs(root, cur_sum):
            if not root:
                return 
            cur_sum += root.val
            self.ans += cache[cur_sum - targetSum]
            cache[cur_sum] += 1
            dfs(root.left, cur_sum)
            dfs(root.right, cur_sum)
            cache[cur_sum] -= 1
            
        dfs(root, 0)
        return self.ans