from typing import List

def profitableSchemes(n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
    # memo = {}
    # n_groups = len(group)

    # def dfs(i, remain_n, current_profit):
    #     if remain_n < 0:
    #         return 0
        
    #     if i == n_groups:
    #         return 1 if current_profit >= minProfit else 0
        
    #     if (i, remain_n, min(current_profit, minProfit)) in memo:
    #         return memo[(i, remain_n, min(current_profit, minProfit))]
        
    #     memo[(i, remain_n, min(current_profit, minProfit))] = (dfs(i+1, remain_n-group[i], current_profit+profit[i]) + dfs(i+1, remain_n, current_profit))%(10**9+7)
    #     return memo[(i, remain_n, min(current_profit, minProfit))]

    # return dfs(0, n, 0)

    # dp[i][j]: total i profit, j number of people used
    dp = [[0] * (n+1) for _ in range(minProfit+1)]
    dp[0][0] = 1 # for 0 profit, 0 members there are total 1 way to select

    for i in range(1, n+1):
        for j in range(1, minProfit+1):
            

n = 5
minProfit = 3
group = [2,2]
profit = [2,3]
print(profitableSchemes(n, minProfit, group, profit))
# Output: 2

n = 10
minProfit = 5
group = [2,3,5]
profit = [6,7,8]
print(profitableSchemes(n, minProfit, group, profit))
# Output: 7