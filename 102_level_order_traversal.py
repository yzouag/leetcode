from typing import Optional, List
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def levelOrder(root: Optional[TreeNode]) -> List[List[int]]:
    res = []

    if not root:
        return res

    stack = deque([root])
    
    while stack:
        nextStack = deque([])
        level_res = []
        while stack:
            node = stack.popleft()
            level_res.append(node.val)
            if node.left: nextStack.append(node.left)
            if node.right: nextStack.append(node.right)
        stack = nextStack
        res.append(level_res)
    
    return res