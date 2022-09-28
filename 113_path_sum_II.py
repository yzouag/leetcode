from typing import Optional, List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []

        def dfs(node: Optional[TreeNode], current_path: List[int], current_sum: int) -> None:
            current_path.append(node.val)
            if not node.left and not node.right:
                if current_sum + node.val == targetSum:
                    result.append(current_path.copy())
            else:
                if node.left:
                    dfs(node.left, current_path, current_sum+node.val)
                if node.right:
                    dfs(node.right, current_path, current_sum+node.val)
            current_path.pop()
        
        result = []
        dfs(root, [], 0)
        return result