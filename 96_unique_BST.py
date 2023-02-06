# numTrees(n) = F(1, n) + F(2, n) + ... + F(n, n) 
# where F(j, n) means n nodes but root node is j
# for each F(i, n), the left and right tree is 1 to (j-1) and (j+1) to n
# the possible counts of left and right tree will be numTrees(j-1), numTrees(n-j)

def numTrees(n: int) -> int:
    # two base case
    if n == 1:
        return 1
    if n == 2:
        return 2
    
    res = [1, 1, 2] + [0] * (n-2)
    for i in range(3, n+1):
        for j in range(1, i+1):
            left = res[j-1]
            right = res[i-j]
            res[i] += left * right
    return res[-1]

n = 3
print(numTrees(n)) # 5

n = 1
print(numTrees(n)) # 1
