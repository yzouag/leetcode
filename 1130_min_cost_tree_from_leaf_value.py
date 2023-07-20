from typing import List, Tuple
# slow DP solution
# time complexity:
# O(N^2) momo, O(N) to find each memo so O(N^3) complexity
# def mctFromLeafValues(arr: List[int]) -> int:
#     memo = {}
    
#     def dp(i, j) -> Tuple[int, int]:
#         if i == j:
#             return 0, arr[i]
        
#         if (i, j) in memo:
#             return memo[(i, j)]
        
#         min_sum = float('inf')
#         for k in range(i, j):
#             left_sum, left_max_leaf = dp(i, k)
#             right_sum, right_max_leaf = dp(k+1, j)
#             curr_sum = left_sum + right_sum + left_max_leaf * right_max_leaf
#             if curr_sum < min_sum:
#                 min_sum = curr_sum
#                 max_leaf = max(left_max_leaf, right_max_leaf)
#         memo[(i,j)] = (min_sum, max_leaf)
#         return memo[(i, j)]
    
#     return dp(0,len(arr)-1)[0]

# this question can transform to:
# Given a list A, choose two neighbors in the array a, b.
# remove the smaller one min(a, b) with cost a*b
# what is min cost to remove all elements until only one left
def mctFromLeafValues(arr: List[int]) -> int:
    res = 0
    stack = [float('inf')]
    for a in arr:
        while stack[-1] <= a:
            mid = stack.pop()
            res += mid * min(stack[-1], a)
        stack.append(a)
    while len(stack) > 2:
        res += stack.pop() * stack[-1]
    return res

arr = [6,2,4]
print(mctFromLeafValues(arr))
# Output: 32

arr = [4,11]
print(mctFromLeafValues(arr))
# Output: 44

arr = [3,8,5,2]
print(mctFromLeafValues(arr))
# Output: 74