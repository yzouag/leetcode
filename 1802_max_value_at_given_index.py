def maxValue(n: int, index: int, maxSum: int) -> int:
    min_possible = 1
    max_possible = maxSum

    def get_total(max_val: int):
        res = 0
        l = max(1, max_val - index)
        res += (l+max_val)*(max_val-l+1)//2
        if max_val-index < 1:
            res += index-max_val+1
        r = max(1, max_val-(n-index-1))
        res += (r+max_val)*(max_val-r+1)//2
        if max_val-n+index+1 < 1:
            res += n-index-max_val
        return res - max_val
    
    while min_possible < max_possible:
        mid = (max_possible + min_possible)//2
        curr_sum = get_total(mid)
        if curr_sum > maxSum:
            max_possible = mid - 1
        elif curr_sum == maxSum:
            return mid
        else:
            min_possible = mid + 1
    
    if get_total(min_possible) > maxSum:
        return min_possible-1
    return min_possible

n = 4
index = 2
maxSum = 6
print(maxValue(n, index, maxSum))
# Output: 2

n = 6
index = 1
maxSum = 10
print(maxValue(n, index, maxSum))
# Output: 3