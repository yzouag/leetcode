from typing import List

def diffWaysToCompute(input, memo={}):
    def helper(m, n, op):
        if op == "+":
            return m+n
        elif op == "-":
            return m-n
        else:
            return m*n

    if input.isdigit():
        return [int(input)]
    if input in memo:
        return memo[input] 
    res = []
    for i in range(len(input)):
        if input[i] in "-+*":
            res1 = diffWaysToCompute(input[:i])
            res2 = diffWaysToCompute(input[i+1:])
            for j in res1:
                for k in res2:
                    res.append(helper(j, k, input[i]))
    memo[input] = res
    return res

expression = "2-1-1"
print(diffWaysToCompute(expression))
# Output: [0,2]

expression = "2*3-4*5"
print(diffWaysToCompute(expression))
# Output: [-34,-14,-10,-10,10]