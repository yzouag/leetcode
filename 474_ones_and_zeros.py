from typing import List
from collections import Counter
def findMaxForm(strs: List[str], m: int, n: int) -> int:
    memo_counts = {}
    memo = {}
    def dfs(i, m_remains, n_remains):
        if i == len(strs):
            return 0
        
        if (i, m_remains, n_remains) in memo:
            return memo[(i, m_remains, n_remains)]
        
        if i in memo_counts:
            n0, n1 = memo_counts[i]
        else:
            c = Counter(strs[i])
            n0 = c['0']
            n1 = c['1']
            memo_counts[i] = (n0, n1)

        res = [dfs(i+1, m_remains, n_remains)]
        if n0 <= m_remains and n1 <= n_remains:
            res.append(dfs(i+1, m_remains-n0, n_remains-n1)+1)
        memo[(i, m_remains, n_remains)] = max(res)
        return memo[(i, m_remains, n_remains)]
    return dfs(0, m, n)
        
        


strs = ["10","0001","111001","1","0"]
m = 5
n = 3
print(findMaxForm(strs, m, n))
# Output: 4

strs = ["10","0","1"]
m = 1
n = 1
print(findMaxForm(strs, m, n))
# Output: 2

strs = ["111","1000","1000","1000"]
m = 9
n = 3
print(findMaxForm(strs, m, n))
# Output: 3

strs = ["10","0001","111001","1","0"]
m = 50
n = 30
print(findMaxForm(strs, m, n))
# Output: 5
