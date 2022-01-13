from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        if n == k:
            return [list(range(1, k+1))]
        if k == 1:
            return [[i] for i in range(1, n+1)]
        
        # option 1: exclude n
        exclude_n = self.combine(n-1, k)
        
        # option 2: contain n
        include_n = self.combine(n-1, k-1)
        include_n = [i + [n] for i in include_n]
        exclude_n.extend(include_n)
        return exclude_n

if __name__ == "__main__":
    n = 4
    k = 2
    print(Solution().combine(n, k))
