from typing import List


def findSubsequences(nums: List[int]) -> List[List[int]]:
    res = []
    
    def dfs(index, running):
        if len(running) >= 2:
            res.append(running)     
        dup_bag = set()
        for i in range(index+1, len(nums)):    
            if nums[i] >= nums[index] and nums[i] not in dup_bag:    
                dfs(i,running+[nums[i]])    
            dup_bag.add(nums[i])      
    
    ib = set()
    for k in range(len(nums)):
        if nums[k] not in ib:
            dfs(k,[nums[k]])
        ib.add(nums[k])
        
    return res 

nums = [4,6,7,7]
print(findSubsequences(nums))
# [[4,6],[4,6,7],[4,6,7,7],[4,7],[4,7,7],[6,7],[6,7,7],[7,7]]

nums = [4,4,3,2,1]
print(findSubsequences(nums))
# [[4,4]]