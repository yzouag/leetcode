def numTilings(n: int) -> int:
    if n <= 2: return n
    filled_prev, gap_prev, filled_prev2, gap_prev2 = 2,2,1,1
    for i in range(3, n+1):
        filled = filled_prev + filled_prev2 + 2*gap_prev2
        gap = filled_prev + gap_prev
        
        filled_prev2, filled_prev, gap_prev2, gap_prev = filled_prev, filled, gap_prev, gap
    return filled_prev % 1_000_000_007

n = 3
print(numTilings(n))
# Output: 5

n = 1
print(numTilings(n))
# Output: 1