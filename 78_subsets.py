from typing import List

def subsets(nums: List[int]) -> List[List[int]]:
    def backTrack(start, cur_list):
        ans.append(cur_list[:])
        
        for j in range(start, n):
            cur_list.append(nums[j])
            backTrack(j+1, cur_list)
            cur_list.pop()
    
    n = len(nums)
    ans = []

    backTrack(0, [])  
    return ans

nums = [1,2,3]
print(subsets(nums))
# Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

nums = [0]
print(subsets(nums))
# Output: [[],[0]]