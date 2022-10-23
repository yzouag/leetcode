from collections import defaultdict
from typing import List


def calcEquation(equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
    adjacent_list = defaultdict(list)
    for equation, value in zip(equations, values):
        adjacent_list[equation[0]].append((equation[1],value))
        adjacent_list[equation[1]].append((equation[0],1/value))

    def dfs(node: str, target: str, value: float, visited: set)-> float:
        if node == target:
            return value
        for neighbor, weight in adjacent_list[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                res = dfs(neighbor, target, value*weight, visited)
                if res != -1:
                    return res
        return -1
    
    res = []
    for x, y in queries:
        if x not in adjacent_list or y not in adjacent_list:
            res.append(-1)
        elif x == y:
            res.append(1)
        else:
            visited = set()
            res.append(dfs(x, y, 1, visited))
    return res
    

equations = [["a","b"],["b","c"]]
values = [2.0,3.0]
queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
print(calcEquation(equations, values, queries))
# Output: [6.00000,0.50000,-1.00000,1.00000,-1.00000]

equations = [["a","b"],["b","c"],["bc","cd"]]
values = [1.5,2.5,5.0]
queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]
print(calcEquation(equations, values, queries))
# Output: [3.75000,0.40000,5.00000,0.20000]

equations = [["a","b"]]
values = [0.5]
queries = [["a","b"],["b","a"],["a","c"],["x","y"]]
print(calcEquation(equations, values, queries))
# Output: [0.50000,2.00000,-1.00000,-1.00000]