from typing import List
from collections import deque

def eventualSafeNodes(graph: List[List[int]]) -> List[int]:
    num_nodes = len(graph)
    out_edge = []

    terminal_nodes = deque([])
    safe_nodes = []

    parent_nodes = [[] for _ in range(num_nodes)]

    for i, to_nodes in enumerate(graph):
        out_edge.append(len(to_nodes))
        if len(to_nodes) == 0:
            terminal_nodes.append(i)
        for node in to_nodes:
            parent_nodes[node].append(i)
    
    while terminal_nodes:
        node = terminal_nodes.popleft()
        safe_nodes.append(node)

        for p_node in parent_nodes[node]:
            out_edge[p_node] -= 1
            if out_edge[p_node] == 0:
                terminal_nodes.append(p_node)

    safe_nodes.sort()
    return safe_nodes


graph = [[1,2],[2,3],[5],[0],[5],[],[]]
print(eventualSafeNodes(graph))
# Output: [2,4,5,6]

graph = [[1,2,3,4],[1,2],[3,4],[0,4],[]]
print(eventualSafeNodes(graph))
# Output: [4]