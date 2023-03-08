from typing import Optional, List
from collections import defaultdict

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # serialize the tree to check if they are the same
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        seen = defaultdict(list)
        def traverse(node: Optional[TreeNode]):
            if not node:
                return "nil"
            tree = f'{node.val},{traverse(node.left)},{traverse(node.right)}'
            seen[tree].append(node)
            return tree
        traverse(root)
        result = []
        for tree in seen:
            if len(seen[tree]) > 1:
                result.append(seen[tree][0])
        return result