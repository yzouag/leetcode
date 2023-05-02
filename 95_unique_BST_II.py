from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        memo = {}
        def dp(i, j):
            if i > j:
                return []
            if i == j:
                return [TreeNode(val=i)]
            
            if (i,j) in memo:
                return memo[(i,j)]
            
            res = []
            for nn in range(i, j+1):
                left = dp(i, nn-1)
                right = dp(nn+1, j)
                if not left:
                    for jj in range(len(right)):
                        node = TreeNode(nn)
                        node.right = right[jj]
                        res.append(node)
                    continue
                if not right:
                    for ii in range(len(left)):
                        node = TreeNode(nn)
                        node.left = left[ii]
                        res.append(node)
                    continue
                
                for ii in range(len(left)):
                    for jj in range(len(right)):
                        node = TreeNode(nn)
                        node.left = left[ii]
                        node.right = right[jj]
                        res.append(node)
            memo[(i,j)] = res
            return res
            
        return dp(1, n)