from collections import defaultdict, deque
from typing import List


class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        # depth first search
        # res = []
        # def dfs(n: int, num: int, last_digit: int) -> None:
        #     nonlocal res
        #     if n == 0: # process all digits
        #         res.append(num)
        #         return
        #     next_digits = set([last_digit+k, last_digit-k])
        #     for next_digit in next_digits:
        #         if 0 <= next_digit < 10:
        #             dfs(n-1, num*10+next_digit, next_digit)
        
        # for i in range(1, 10):
        #     dfs(n-1, i, i)
        # return res

        # breadth first search
        queue = deque([])
        for i in range(1, 10):
            queue.append(i)

        for i in range(n-1):
            next_queue = deque([])
            while queue:
                num = queue.popleft()
                last_digit = num%10
                next_digits = set([last_digit+k, last_digit-k])
                for next_digit in next_digits:
                    if 0 <= next_digit < 10:
                        next_queue.append(num*10 + next_digit)
            queue = next_queue
        return queue

if __name__ == "__main__":
    n = 3
    k = 7
    # [181,292,707,818,929]
    print(Solution().numsSameConsecDiff(n, k))

    n = 2
    k = 1
    # [10,12,21,23,32,34,43,45,54,56,65,67,76,78,87,89,98]
    print(Solution().numsSameConsecDiff(n, k))