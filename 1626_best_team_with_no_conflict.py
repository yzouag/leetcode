from typing import List
def bestTeamScore(scores: List[int], ages: List[int]) -> int:
    players = list(zip(ages, scores))
    players.sort()
    
    dp = [0] * len(players)
    dp[0] = players[0][1] # denote dp as the highest score include player i
    for i in range(1, len(players)):
        # if players[i][0] == players[i-1][0] or players[i][1] > players[i-1][1]: # same age or higher score, just include him
        #     dp[i] = dp[i-1] + players[i][1]
        #     continue
        for j in range(i):
            if players[j][1] <= players[i][1]:
                dp[i] = max(dp[i], dp[j])
        dp[i] += players[i][1]
    return max(dp)

scores = [1,3,5,10,15]
ages = [1,2,3,4,5]
print(bestTeamScore(scores, ages)) # 34

scores = [4,5,6,5]
ages = [2,1,2,1]
print(bestTeamScore(scores, ages)) # 16

scores = [1,2,3,5]
ages = [8,9,10,1]
print(bestTeamScore(scores, ages)) # 6