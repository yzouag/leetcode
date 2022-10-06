from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def hasPathSum(root: Optional[TreeNode], targetSum: int) -> bool:
    if not root:
        return False
    def dfs(node: TreeNode, targetSum: int) -> bool:
        if not node.left and not node.right:
            return targetSum == 0
        res = False
        if node.left:
            res = res or dfs(node.left, targetSum-node.val)
        if node.right:
            res = res or dfs(node.right, targetSum-node.val)
        return res
    return dfs(root, targetSum)