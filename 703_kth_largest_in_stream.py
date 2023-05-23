from typing import List
import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        heapq.heapify(nums)
        self.nums = nums
        self.k = k

        for _ in range(k, len(nums)):
            heapq.heappop(self.nums)

    def add(self, val: int) -> int:
        heapq.heappush(self.nums, val)
        if len(self.nums) > self.k:
            heapq.heappop(self.nums)
        return self.nums[0]

kthLargest = KthLargest(3, [4, 5, 8, 2])
kthLargest.add(3) # return 4
kthLargest.add(5) # return 5
kthLargest.add(10)# return 5
kthLargest.add(9) # return 8
kthLargest.add(4) # return 8