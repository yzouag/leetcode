from typing import List

def twoCitySchedCost(costs: List[List[int]]) -> int:
    differences = list(map(lambda x: (x[0]-x[1], x[0], x[1]), costs))
    differences.sort(key=lambda x: abs(x[0]), reverse=True)
    
    A, B = 0, 0
    n = len(costs) // 2
    total_cost = 0
    for diff, cost_a, cost_b in differences:
        if A == n:
            total_cost += cost_b
        elif B == n:
            total_cost += cost_a
        else:
            if diff > 0:
                B += 1
                total_cost += cost_b
            else:
                A += 1
                total_cost += cost_a
    return total_cost


costs = [[10,20],[30,200],[400,50],[30,20]]
print(twoCitySchedCost(costs))
# Output: 110

costs = [[259,770],[448,54],[926,667],[184,139],[840,118],[577,469]]
print(twoCitySchedCost(costs))
# Output: 1859

costs = [[515,563],[451,713],[537,709],[343,819],[855,779],[457,60],[650,359],[631,42]]
print(twoCitySchedCost(costs))
# Output: 3086