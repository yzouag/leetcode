from typing import List, Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left:Optional['TreeNode']=None, right:Optional['TreeNode']=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        mapping = {value: i for i, value in enumerate(inorder)}
        self.root_id = 0
        def build(start, end):
            if start > end:
                return None
            root_val = preorder[self.root_id]
            self.root_id += 1
            root = TreeNode(root_val)
            root.left = build(start, mapping[root_val]-1)
            root.right = build(mapping[root_val]+1, end)
            return root
        return build(0, len(preorder)-1)

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
# Output: [3,9,20,null,null,15,7]

preorder = [-1]
inorder = [-1]
# Output: [-1]