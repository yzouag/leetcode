from collections import deque
from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        # BFS
        q, ans = [root], []
        while len(q):
            qlen, row = len(q), 0
            for _ in range(qlen):
                curr = q.pop(0)
                row += curr.val
                if curr.left: q.append(curr.left)
                if curr.right: q.append(curr.right)
            ans.append(row/qlen)
        return ans

        # DFS
        # info = []
        # def dfs(node, depth = 0):
        #     if node:
        #         if len(info) <= depth:
        #             info.append([0, 0])
        #         info[depth][0] += node.val
        #         info[depth][1] += 1
        #         dfs(node.left, depth + 1)
        #         dfs(node.right, depth + 1)
        # dfs(root)

        # return [s/float(c) for s, c in info]
