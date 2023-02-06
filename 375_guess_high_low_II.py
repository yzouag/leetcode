def getMoneyAmount(n: int) -> int:
    arr = [[0] * (n+1) for _ in range(n+1)]
    for i in range(1, n):
        for j in range(1, n-i+1):
            minimum = float('inf')
            for k in range(j, j+i+1):
                left = arr[j][k-1] if k-1 >= j else 0
                right = arr[k+1][j+i] if k+1 <= j+i else 0
                minimum = min(minimum, k + max(left, right))
            arr[j][j+i] = minimum
    return arr[1][n]


n = 10
print(getMoneyAmount(n)) # 16

n = 1
print(getMoneyAmount(n)) # 0

n = 2
print(getMoneyAmount(n)) # 1