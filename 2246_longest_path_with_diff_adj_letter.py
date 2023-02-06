from typing import List, Tuple
from collections import defaultdict
import heapq
def longestPath(parent: List[int], s: str) -> int:
    adjacent_list = defaultdict(list)
    for i in range(1, len(parent)):
        adjacent_list[parent[i]].append(i)
    
    def dfs(node: int) -> Tuple[int, int]:
        # return: longest_path (can be a path in subtree, it must be longest) our answer
        #         longest link (must include current node)
        
        # leaf node
        if len(adjacent_list[node]) == 0:
            return 1, 1

        longest_path = 0
        longest_link = [0, 0] # use a heap to store two largest links (without current node)

        for descendant in adjacent_list[node]:
            l_path, l_link = dfs(descendant)
            # if this link has a different head with current node
            # update this link to potential longest two links
            if s[descendant] != s[node]: 
                heapq.heappushpop(longest_link, l_link)
            longest_path = max(longest_path, l_path)
        
        # check the longest path is from subtree
        # or it is a path include current node with two longest links
        longest_path = max(longest_path, sum(longest_link)+1) 
        longest_link = max(longest_link) + 1 # only return the longest link
        
        return longest_path, longest_link
    
    return dfs(0)[0]

parent = [-1,0,0,1,1,2]
s = "abacbe"
print(longestPath(parent, s)) # 3

parent = [-1,0,0,0]
s = "aabc"
print(longestPath(parent, s)) # 3
