# def backtracking(problem):
#     def reject(candidate):
#         # returns True if the partial candidate solution can be rejected
    
#     def accept(candidate):
#         # returns True if the candidate solution is a full solution

#     def children(candidate):
#         # returns all possible candidate solutions that can be generated from the current candidate solution

#     def dfs(candidate):
#         if reject(candidate):
#             return
#         if accept(candidate):
#             print(candidate) # more generally, you can append the accepted solution to an output array
#             return
#         for child in children(candidate):
#             dfs(child)
#    root = ... # root is whatever the starting partial candidate solution is. In this case, it would be having placed 0 .s.
#    dfs(root)

from typing import List

def restoreIpAddresses(s: str) -> List[str]:
    def valid_ip_part(s: str) -> bool:
        if s[0] == '0':
            return len(s) == 1
        return int(s) < 256

    res = []
    def dfs(num_of_parts: int, s: str, ip: str) -> None:
        # base case
        if num_of_parts == 1:
            if valid_ip_part(s):
                res.append(ip[1:] + '.' + s)
        
        # recursion
        for i in range(1, min(4, len(s))):
            if valid_ip_part(s[:i]):
                dfs(num_of_parts-1, s[i:], ip + '.' + s[:i])
    
    dfs(4, s, '')
    return res

s = "25525511135"
print(restoreIpAddresses(s)) # ["255.255.11.135","255.255.111.35"]

s = "0000"
print(restoreIpAddresses(s)) # ["0.0.0.0"]

s = "101023"
print(restoreIpAddresses(s)) # ["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]