from typing import List

def findJudge(n: int, trust: List[List[int]]) -> int:
    being_trusted = [0] * (n+1)
    trust_other = [False] * (n+1)
    for a, b in trust:
        being_trusted[b] += 1
        trust_other[a] = True

    for i in range(1, n+1):
        if being_trusted[i] == (n-1) and trust_other[i] == False:
            return i
    return -1

n = 2
trust = [[1,2]]
print(findJudge(n, trust)) # 2

n = 3
trust = [[1,3],[2,3]]
print(findJudge(n, trust)) # 3

n = 3
trust = [[1,3],[2,3],[3,1]]
print(findJudge(n, trust)) # -1