import heapq
from typing import List

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        # method 1: using a min heap (built-in function)
        # min_heap = []
        # for i in range(len(matrix)):
        #     for j in range(len(matrix[0])):
        #         if len(min_heap) >= k:
        #             # the largest in matrix will be smallest in the heap
        #             # it will be popped out, so at last we will have the kth largest
        #             heapq.heappushpop(min_heap, -matrix[i][j])
        #         else:
        #             heapq.heappush(min_heap, -matrix[i][j])
        # return -heapq.heappop(min_heap)

        # method 2: using a max heap
        # gradually expand, put the candidates in the heap
        # pop the smallest one, this will be the kth smallest in the matrix
        # expand k times until we get the result
        # candidate_heap = [] # why use heap? Because find smallest in heap and update only cost log(n)
        # for i in range(len(matrix)):
        #     heapq.heappush(candidate_heap, (matrix[i][0], i, 0))
        # for i in range(k):
        #     res, row, column = heapq.heappop(candidate_heap)
        #     if column < len(matrix[0]) - 1: # how we expand? We only need to put the next element in the same row to the candidate list
        #         heapq.heappush(candidate_heap, (matrix[row][column+1], row, column+1)) # this one must be the only candidate
        # return res

        # method 3: use binary search
        pass

if __name__ == "__main__":
    matrix = [[1,5,9],
              [10,11,13],
              [12,13,15]]
    k = 8
    assert Solution().kthSmallest(matrix, k) == 13

    matrix = [[-5]]
    k = 1
    assert Solution().kthSmallest(matrix, k) == -5
