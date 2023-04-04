# Sieve of Eratosthenes
# 1. Create a list of consecutive integers from 2 through n: (2, 3, 4, ..., n).
# 2. Initially, let p equal 2, the smallest prime number.
# 3. Enumerate the multiples of p by counting in increments of p from 2p to n, and mark them in the list (these will be 2p, 3p, 4p, ...; the p itself should not be marked).
# 4. Find the smallest number in the list greater than p that is not marked. If there was no such number, stop. Otherwise, let p now equal this new number (which is the next prime), and repeat from step 3.
# 5. When the algorithm terminates, the numbers remaining not marked in the list are all the primes below n.

def countPrimes(n: int) -> int:
    nums = list(range(1, n))
    for i in range(1, len(nums)):
        if nums[i] < 0:
            continue
        k = 2
        while True:
            if nums[i] * k < n:
                if nums[nums[i]*k-1] > 0:
                    nums[nums[i]*k-1] = -nums[nums[i]*k-1]
                k += 1
            else:
                break
    counts = 0
    for num in nums[1:]:
        if num > 0:
            counts += 1
    return counts


n = 10
print(countPrimes(n))
# Output: 4

n = 0
print(countPrimes(n))
# Output: 0

n = 1
print(countPrimes(n))
# Output: 0

n = 3
print(countPrimes(n))
# Output: 1