from typing import List

def maximumRequests(n: int, requests: List[List[int]]) -> int:
    num_employees_transfer = [0] * n
    max_requests = 0
    num_requests = len(requests)
    def dfs(index, requests_accepted):
        nonlocal max_requests
        if index == num_requests:
            if all(v == 0 for v in num_employees_transfer):
                max_requests = max(max_requests, requests_accepted)
            return
        move_out, move_in = requests[index]
        num_employees_transfer[move_out] -= 1
        num_employees_transfer[move_in] += 1
        dfs(index+1, requests_accepted+1)
        num_employees_transfer[move_out] += 1
        num_employees_transfer[move_in] -= 1
        dfs(index+1, requests_accepted)
    dfs(0, 0)
    return max_requests
        

n = 5
requests = [[0,1],[1,0],[0,1],[1,2],[2,0],[3,4]]
print(maximumRequests(n, requests))
# Output: 5

n = 3
requests = [[0,0],[1,2],[2,1]]
print(maximumRequests(n, requests))
# Output: 3

n = 4
requests = [[0,3],[3,1],[1,2],[2,0]]
print(maximumRequests(n, requests))
# Output: 4