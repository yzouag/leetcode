from typing import List
def summaryRanges(nums: List[int]) -> List[str]:
    res = []
    i = 0

    # key design: using two while loop, to step through i
    while i < len(nums):
        start = nums[i]
        while i+1 < len(nums) and nums[i+1]-nums[i] == 1:
            i += 1
        if nums[i] == start:
            res.append(str(start))
        else:
            res.append(f'{start}->{nums[i]}')
        i += 1
    return res
    


nums = [0,1,2,4,5,7]
print(summaryRanges(nums))
# Output: ["0->2","4->5","7"]

nums = [0,2,3,4,6,8,9]
print(summaryRanges(nums))
# Output: ["0","2->4","6","8->9"]