from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        # if not root:
        #     return False
        
        # queue = [root]
        # endLevel = False
        # while queue:
        #     temp = []
        #     if not endLevel:
        #         for node in queue:
        #             if not endLevel:
        #                 if node.right and not node.left:
        #                     return False
        #                 if not node.right:
        #                     if node.left:
        #                         temp.append(node.left)
        #                     endLevel = True     
        #                 elif node.left and node.right:
        #                     temp.append(node.left)
        #                     temp.append(node.right)
        #             else:
        #                 if node.left or node.right:
        #                     return False
        #     else:
        #         for node in queue:
        #             if node.left or node.right:
        #                 return False
        #         break
        #     queue = temp
                
        # return True

        if not root:
            return False
        
        queue = [root]
        nullNodeFound = False
        while queue:
            temp = []
            for node in queue:
                if not node:
                    nullNodeFound = True
                else:
                    if nullNodeFound:
                        return False
                    temp.append(node.left)
                    temp.append(node.right)
            queue = temp
                
        return True