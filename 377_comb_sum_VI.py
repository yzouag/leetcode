from typing import List
def combinationSum4(nums: List[int], target: int) -> int:
    memo = {}
    nums.sort(reverse=True)
    def dfs(remain):
        if remain in memo:
            return memo[remain]
        counts = 0
        for num in nums:
            if remain > num:
                counts += dfs(remain-num)
            elif remain == num:
                counts += 1
        memo[remain] = counts
        return counts
    return dfs(target)

nums = [1,2,3]
target = 4
print(combinationSum4(nums, target))
# Output: 7

nums = [9]
target = 3
print(combinationSum4(nums, target))
# Output: 0