from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        first_element_ptr = 0
        min_diff = 20000
        while first_element_ptr < len(nums) - 2:
            new_target = target - nums[first_element_ptr]
            second_element_ptr = first_element_ptr + 1
            third_element_ptr = len(nums) - 1
            while second_element_ptr < third_element_ptr:
                current_diff = new_target - (nums[second_element_ptr] + nums[third_element_ptr])
                if current_diff < 0:
                    third_element_ptr -= 1
                elif current_diff > 0:
                    second_element_ptr += 1
                else:
                    return target
                if abs(current_diff) < abs(min_diff):
                    min_diff = current_diff
            first_element_ptr += 1
        return target - min_diff

if __name__ == "__main__":
    nums = [-1,2,1,-4]
    target = 1
    assert 2 == Solution().threeSumClosest(nums, target)

    nums = [0,0,0]
    target = 1
    assert 0 == Solution().threeSumClosest(nums, target)