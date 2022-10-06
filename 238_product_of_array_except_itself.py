from typing import List

def productExceptSelf(nums: List[int]) -> List[int]:
    # note, if we don't want to use divide, then just use prefix product and suffix product
    count_of_zero = 0
    product = 1
    zero_index = -1
    for index, num in enumerate(nums):
        if num == 0:
            count_of_zero += 1
            zero_index = index
            continue
        product *= num
    
    if count_of_zero > 1:
        return [0]* len(nums)
    
    if count_of_zero == 1:
        res = [0]*len(nums)
        res[zero_index] = product
        return res

    res = []
    for num in nums:
        res.append(product//num)
    return res


nums = [1,2,3,4]
print(productExceptSelf(nums))
# Output: [24,12,8,6]

nums = [-1,1,0,-3,3]
print(productExceptSelf(nums))
# Output: [0,0,9,0,0]