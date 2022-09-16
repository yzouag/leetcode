from collections import deque
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        # method 1: recursion
        # if not root:
        #     return ''
        # right = self.tree2str(root.right)
        # left = self.tree2str(root.left)
        # if not left and not right:
        #     return f'{root.val}'
        # if not right:
        #     return f'{root.val}({left})'
        # return f'{root.val}({left})({right})'

        # method 2: stack
        # if not root:
        #     return ''
        result = ''
        visited = set()
        stack = [root]
        while stack:
            node = stack[-1]
            if node not in visited:
                visited.add(node)
                result += f'({node.val}'
                if not node.left and node.right:
                    result += '()'
                if node.right:
                    stack.append(node.right)
                if node.left:
                    stack.append(node.left)
            else:
                stack.pop()
                result += ')'
        return result[1:-1]