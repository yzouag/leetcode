from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def addOneRow(root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
    if depth == 1:
        return TreeNode(val, left=root)
    
    nodes_in_upper_layer = [root, None]
    for _ in range(depth-2):
        while True:
            node = nodes_in_upper_layer.pop(0)
            if node == None:
                nodes_in_upper_layer.append(None)
                break
            if node.left:
                nodes_in_upper_layer.append(node.left)
            if node.right:
                nodes_in_upper_layer.append(node.right)
    
    for node in nodes_in_upper_layer[:-1]:
        node.left = TreeNode(val, node.left)
        node.right = TreeNode(val, None, node.right)
    return root
