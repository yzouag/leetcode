from typing import List
import bisect

class SummaryRanges:

    def __init__(self):
        self.nums = []
        self.all_nums = set()
        

    def addNum(self, value: int) -> None:
        # i, j = 0, len(self.intervals)-1
        if value in self.all_nums:
            return
        self.all_nums.add(value)
        bisect.insort_left(self.nums, value)
        

    def getIntervals(self) -> List[List[int]]:
        if not self.nums:
            return []
        
        res = []
        left = right = self.nums[0]
        for i in range(1, len(self.nums)):
            if self.nums[i] != self.nums[i-1] + 1:
                res.append([left, right])
                left = right = self.nums[i]
            else:
                right = self.nums[i]
        res.append([left, right])
        return res


# Your SummaryRanges object will be instantiated and called as such:
summaryRanges = SummaryRanges()
summaryRanges.addNum(1)
summaryRanges.getIntervals()
summaryRanges.addNum(3)
summaryRanges.getIntervals()
summaryRanges.addNum(7)
summaryRanges.getIntervals()
summaryRanges.addNum(2)
summaryRanges.getIntervals()
summaryRanges.addNum(6)
summaryRanges.getIntervals()
