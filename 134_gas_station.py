from typing import List

# say there are three stations x, y, z (x < y < z)
# conclustion: if from x passing y cannot reach z, then y cannot reach z
# why? when from x go to y, there must be >= 0 gas remains, it cannot go to z
#      just start from y, we have exact 0 remains, so we must not reach z
# so now we start from station 0, if it cannot reach station k
# it means 0 to k-1 cannot go to k, so we just start from k

# the most tricky part is to prove, if total surplus >= 0, then there must 
# exist a path for this question
# prove by contradiction
# assume there is a case where total surplus > 0 but each subsurplus < 0 
# then total surplus < 0, contradicts

def canCompleteCircuit(gas: List[int], cost: List[int]) -> int:
    start = total_surplus = current_surplus = 0
    for i in range(len(gas)):
        current_surplus += gas[i] - cost[i]
        if current_surplus < 0:
            start = i + 1
            current_surplus = 0
        total_surplus += gas[i] - cost[i]
    return -1 if total_surplus < 0 else start

    

gas = [1,2,3,4,5]
cost = [3,4,5,1,2]
print(canCompleteCircuit(gas, cost)) # 3

gas = [2,3,4]
cost = [3,4,3]
print(canCompleteCircuit(gas, cost)) # -1