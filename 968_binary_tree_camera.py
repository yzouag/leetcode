from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# greedy approach
# placing on leaf node is always worse than placing on leaf node's parent
# so every time, find all leaf nodes, get their parents and place camera
# remove all nodes covered and try again
class Solution:
    def minCameraCover(root: Optional[TreeNode]) -> int:
        res = 0
        IS_LEAF = 0
        HAS_CAMERA = 1
        IS_COVERED = 2

        def dfs(node: Optional[TreeNode]):
            nonlocal res
            if not node:
                return IS_COVERED
            l, r = dfs(node.left), dfs(node.right)
            if l == IS_LEAF or r == IS_LEAF: # if its child is a leaf node, place a camera here
                res += 1
                return HAS_CAMERA
            if l == HAS_CAMERA or r == HAS_CAMERA: # if its child has a camera there, this node is covered
                return IS_COVERED
            return IS_LEAF # if no child, or both are leaves

        return (dfs(root) == IS_LEAF) + res # if root node is leaf node, we need to add a camera there