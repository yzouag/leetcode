from collections import defaultdict
from typing import Dict, List

def countSubTrees(n: int, edges: List[List[int]], labels: str) -> List[int]:
    adjacent_matrix = defaultdict(list)

    for edge in edges:
        adjacent_matrix[edge[0]].append(edge[1])
        adjacent_matrix[edge[1]].append(edge[0])

    res = [0] * n
    
    def merge_dict(dic1: Dict[str, int], dic2: Dict[str, int]) -> None:
        for k in dic2:
            if k in dic1:
                dic1[k] += dic2[k]
            else:
                dic1[k] = dic2[k]
    
    visited = set()
    def numOfLabels(node: int) -> Dict[str, int]:
        res_dict = {labels[node]: 1}
        visited.add(node)     
        for neighbor in adjacent_matrix[node]:
            if neighbor not in visited:
                sub_res_dict = numOfLabels(neighbor)
                merge_dict(res_dict, sub_res_dict)
        res[node] = res_dict[labels[node]]
        return res_dict
    numOfLabels(0)
    
    return res
        
    


n = 7
edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]]
labels = "abaedcd"
print(countSubTrees(n, edges, labels)) # Output: [2,1,1,1,1,1,1]

n = 4
edges = [[0,1],[1,2],[0,3]]
labels = "bbbb"
print(countSubTrees(n, edges, labels)) # Output: [4,2,1,1]

n = 5
edges = [[0,1],[0,2],[1,3],[0,4]]
labels = "aabab"
print(countSubTrees(n, edges, labels)) # [3,2,1,1,1]
