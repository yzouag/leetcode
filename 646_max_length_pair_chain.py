from typing import List

def findLongestChain(pairs: List[List[int]]) -> int:
    # dp
    # n = len(pairs)
    # pairs.sort(key=lambda x: x[1])
    # dp = [0] * n
    # dp[0] = 1

    # for i in range(n):
    #     start = pairs[i][0]
    #     for j in range(i):
    #         if pairs[i-j-1][1] < start:
    #             dp[i] = max(dp[i], dp[i-j-1]+1)
    # return max(dp)

    # solve using greedy
    # sort by second element
    # why always work?
    # say there are two pairs A (A_s, A_e), B (B_s, B_e)
    # assume A_e < B_e
    # so we will consider A first
    # if A_e < B_s, we definitely can include A
    # else
    #  assume A_s, B_s both larger than previous pair
    #  it must be better to choose A_e, so that later paris are more likely to be compatible
    pairs.sort(key=lambda x: x[1])
    curr = float('-inf')
    ans = 0

    for pair in pairs:
        if pair[0] > curr:
            ans += 1
            curr = pair[1]
    return ans


pairs = [[1,2],[2,3],[3,4]]
print(findLongestChain(pairs))
# Output: 2

pairs = [[1,2],[7,8],[4,5]]
print(findLongestChain(pairs))
# Output: 3