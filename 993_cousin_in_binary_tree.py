from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isCousins(root: Optional[TreeNode], x: int, y: int) -> bool:
    q = [root]
    while q:
        temp = []
        detect_x = detect_y = False
        for node in q:
            if not node:
                continue
            if node.left and node.left.val == x and node.right and node.right.val == y:
                return False
            if node.left and node.left.val == y and node.right and node.right.val == x:
                return False
            temp.extend([node.left, node.right])
            if node.val == x:
                detect_x = True
            elif node.val == y:
                detect_y = True
        if detect_x ^ detect_y:
            return False
        if detect_x == detect_y and detect_x == True:
            return True
        q = temp
    return False