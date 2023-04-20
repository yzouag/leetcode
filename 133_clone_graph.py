# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        
        visited = {}

        def copy_node(node: 'Node') -> 'Node':
            if node in visited:
                return visited[node]
            
            new_node = Node(val=node.val)
            visited[node] = new_node
            for neighbor in node.neighbors:
                new_node.neighbors.append(copy_node(neighbor))
            
            return new_node

        return copy_node(node)