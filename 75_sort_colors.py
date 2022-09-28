from typing import List

def sortColors(nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    # two pass, count sort
    # red, white, blue = 0, 0, 0
    # for num in nums:
    #     if num == 0:
    #         red += 1
    #     elif num == 1:
    #         white += 1
    #     else:
    #         blue += 1
    # for i in range(len(nums)):
    #     if i <= red-1:
    #         nums[i] = 0
    #     elif i <= red + white -1:
    #         nums[i] = 1
    #     else:
    #         nums[i] = 2
    
    # one pass
    # three pointers
    # red at front, blue at back
    # every time consume a new number, if it is white, not move
    # if red, throw it to the back of red
    # if blue, throw it to the front of blue
    red_ptr, white_ptr, blue_ptr = 0, 0, len(nums)-1
    
    while white_ptr <= blue_ptr:
        if nums[white_ptr] == 1:
            white_ptr += 1
        elif nums[white_ptr] == 0:
            print(white_ptr)
            nums[white_ptr], nums[red_ptr] = nums[red_ptr], nums[white_ptr]
            red_ptr += 1
            white_ptr += 1
        else:
            nums[white_ptr], nums[blue_ptr] = nums[blue_ptr], nums[white_ptr]
            blue_ptr -= 1

sortColors([2,0,1])