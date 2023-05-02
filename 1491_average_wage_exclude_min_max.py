from typing import List
def average(salary: List[int]) -> float:
    return (sum(salary)-min(salary)-max(salary))/(len(salary)-2)

salary = [4000,3000,1000,2000]
print(average(salary))
# Output: 2500.00000

salary = [1000,2000,3000]
print(average(salary))
# Output: 2000.00000