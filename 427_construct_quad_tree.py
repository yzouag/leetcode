from typing import List

class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        
        def helper(grid, row_i, row_j, col_i, col_j) -> Node:
            # base case
            if row_j == row_i + 1:
                return Node(grid[row_i][col_i], 1, None, None, None, None)

            row_mid = (row_i + row_j) // 2
            col_mid = (col_i + col_j) // 2

            node_topLeft = helper(grid, row_i, row_mid, col_i, col_mid)
            node_bottomLeft = helper(grid, row_mid, row_j, col_i, col_mid)
            node_topRight = helper(grid, row_i, row_mid, col_mid, col_j)
            node_bottomRight = helper(grid, row_mid, row_j, col_mid, col_j)

            if node_topLeft.isLeaf + node_topRight.isLeaf + node_bottomLeft.isLeaf + node_bottomRight.isLeaf < 4:
                return Node(1, 0, node_topLeft, node_topRight, node_bottomLeft, node_bottomRight)
            else:
                subgridSum = node_topLeft.val + node_topRight.val + node_bottomLeft.val + node_bottomRight.val
                if subgridSum == 4:
                    return Node(1, 1, None, None, None, None)
                elif subgridSum == 0:
                    return Node(0, 1, None, None, None, None)
                else:
                    return Node(1, 0, node_topLeft, node_topRight, node_bottomLeft, node_bottomRight)
        
        return helper(grid, 0, len(grid), 0, len(grid[0]))


