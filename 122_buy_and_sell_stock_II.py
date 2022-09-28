from typing import List

def maxProfit(prices: List[int]) -> int:
    result = 0
    for i in range(len(prices)-1):
        difference = prices[i+1] - prices[i]
        result += max(0, difference)
    return result
    

prices = [7,1,5,3,6,4]
print(maxProfit(prices))
# Output: 7

prices = [1,2,3,4,5]
print(maxProfit(prices))
# Output: 4

prices = [7,6,4,3,1]
print(maxProfit(prices))
Output: 0