from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# for postorder left -> right -> root
# so the last node will always be the root node
# for inorder traversal left -> root -> right
# we then split it to [left] root [right]
# every node which is larger than the root will be right subtree
# so if one node is on the boundary, it must be a leaf node
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        self.postIdx, mp = len(postorder)-1, {val: idx for idx, val in enumerate(inorder)}
        def build(inStart, inEnd):
            if inStart > inEnd: return None
            root = TreeNode(postorder[self.postIdx])
            self.postIdx -= 1
            root.right = build(mp[root.val]+1, inEnd) # must first right then left, because we traverse it in reverse of postorder
            root.left  = build(inStart, mp[root.val]-1)
            return root        
        return build(0, len(inorder)-1)