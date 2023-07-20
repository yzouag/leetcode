from typing import List
def distributeCookies(cookies: List[int], k: int) -> int:
    smallest_unfair = float('inf')
    n = len(cookies)
    def dfs(i, curr_assigned):
        nonlocal smallest_unfair
        if i == n:
            smallest_unfair = min(smallest_unfair, max(curr_assigned))
            return
        if max(curr_assigned) >= smallest_unfair:
            return 
        for j in range(k):
            curr_assigned[j] += cookies[i]
            dfs(i+1, curr_assigned)
            curr_assigned[j] -= cookies[i]
    dfs(0, [0]*k)
    return smallest_unfair

cookies = [8,15,10,20,8]
k = 2
print(distributeCookies(cookies, k))
# Output: 31

cookies = [6,1,3,2,2,4,1,2]
k = 3
print(distributeCookies(cookies, k))
# Output: 7