from typing import List
import heapq

def nthSuperUglyNumber(n: int, primes: List[int]) -> int:
    nums = primes.copy()
    heapq.heapify(nums)
    p = 1
    for _ in range(n - 1):
        p = heapq.heappop(nums) #take the smallest element
        for prime in primes:
            heapq.heappush(nums, p * prime) # add all those multiples with the smallest number
            if p % prime == 0:  # key step to remove duplication
                break
    return p

n = 12
primes = [2,7,13,19]
print(nthSuperUglyNumber(n, primes))
# Output: 32

n = 1
primes = [2,3,5]
print(nthSuperUglyNumber(n, primes))
# Output: 1