from typing import List

def change(amount: int, coins: List[int]) -> int:
    # c[n, m] = \sum_k c[n-k*m, m-1]

amount = 5
coins = [1,2,5]
print(change(amount, coins)) # 4

amount = 3
coins = [2]
print(change(amount, coins)) # 0

amount = 10
coins = [10]
print(change(amount, coins)) # 1