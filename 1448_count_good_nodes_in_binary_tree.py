# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        path_max = root.val
        return self.dfs(root, path_max, 0)

    def dfs(self, node: TreeNode, path_max: int, count: int) -> int:
        if node.val >= path_max:
            path_max = node.val
            count += 1
        if node.left:
            count += self.dfs(node.left, path_max, 0)
        if node.right:
            count += self.dfs(node.right, path_max, 0)
        return count