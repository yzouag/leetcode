def countOdds(low: int, high: int) -> int:
    return (high + 1) // 2 - low // 2

low = 3
high = 7
print(countOdds(low, high))
# Output: 3

low = 8
high = 10
print(countOdds(low, high))
# Output: 1
