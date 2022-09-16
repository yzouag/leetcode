from collections import deque
from typing import List
"""
# Definition for a Node.
"""
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def levelOrder(self, root: Node) -> List[List[int]]:
        # method 1: bfs
        # if not root:
        #     return []
        # result = []
        # queue = deque([root])
        # while queue:
        #     level_result = []
        #     for _ in range(len(queue)):
        #         node = queue.popleft()
        #         level_result.append(node.val)
        #         queue.extend(node.children)
        #     result.append(level_result)
        # return result

        # method 2: dfs
        if not root:
            return []
        result = []

        def dfs(node: Node, level: int) -> None:
            if not node:
                return
            nonlocal result
            if level > len(result):
                result.append([node.val])
            else:
                result[level-1].append(node.val)
            for child in node.children:
                dfs(child, level+1)
        dfs(root, 1)
        return result