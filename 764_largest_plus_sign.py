from typing import List

def orderOfLargestPlusSign(n: int, mines: List[List[int]]) -> int:
    

n = 5
mines = [[4,2]]
print(orderOfLargestPlusSign(n, mines))
# Output: 2

n = 1
mines = [[0,0]]
print(orderOfLargestPlusSign(n, mines))
# Output: 0