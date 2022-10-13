from collections import defaultdict
import heapq

# a = [3, -1, -4, 1, 2, 5, -3, -2]
a = [3, 2, -5, -6, 1, 4]
negatives = []

sums = 0
counts = 0
for num in a:
    sums += num
    counts += 1
    if num < 0:
        heapq.heappush(negatives, num)
    if sums < 0:
        sums -= heapq.heappop(negatives)
        counts -= 1
print(counts)

initial_players = [1, 2]
new_players = [3, 4]
rank = 2

health = 0
k_largest_heap = []
for i in range(rank):
    heapq.heappush(k_largest_heap, initial_players[i])
for i in range(rank, len(initial_players)):
    heapq.heappushpop(k_largest_heap, initial_players[i])
health += k_largest_heap[0]
for i in new_players:
    heapq.heappushpop(k_largest_heap, i)
    health += k_largest_heap[0]
print(health)

arr = [1, 2, 1, 2]
l = 1
r = 10

def array_generator(arr, l, r):
    brr = [l]
    diff = brr[-1] - arr[0]
    for i in range(1, len(arr)):
        brr_i = max(brr[-1], arr[i]+diff+1)
        if brr_i > r:
            return [-1]
        else:
            brr.append(brr_i)
        diff = brr[-1] - arr[i]
    return brr
print(array_generator(arr, l, r))

arr = [4,2,1,3]
k = 2
def find_integer(arr, k):
    res = []
    k_largest = []
    for i in range(k):
        heapq.heappush(k_largest, arr[i])
    res.append(k_largest[0])
    for i in range(k, len(arr)):
        heapq.heappushpop(k_largest, arr[i])
        res.append(k_largest[0])
    return res
print(find_integer(arr, k))

data = [1, -4, -5, 2]
updates = [[2,4], [1,2]]
counts = [0] * len(data)
for l,r in updates:
    for j in range(l-1, r):
        counts[j] += 1
for i in range(len(data)):
    data[i] *= (-1) ** (counts[i] % 2)
print(data)

vals = [2,3,6,-5,10,1,1]
def even_tag(vals):
    min_odd = 1000000
    res = 0
    for val in vals:
        if val > 0:
            res += val
        if val % 2 != 0:
            if abs(val) < min_odd:
                min_odd = abs(val)
    if res % 2 == 0:
        return res
    else:
        return res - min_odd
print(even_tag(vals))


strings = ["abc", "abcd", "bc", "adc"]
    
def complementary_pairs(strings):
    res = 0
    bits = defaultdict(int)
    for s in strings:
        bitmask = 0
        for c in s:
            bitmask ^= (1 << (ord(c) - ord('a')))
        if bitmask in bits:
            res += bits[bitmask]
        for i in range(26):
            temp = bitmask ^ (1 << i)
            if temp in bits:
                res += bits[temp]
        bits[bitmask] += 1
    return res
print(complementary_pairs(strings))

min_length = 1
max_length = 3
one_group = 1
zero_group = 1
def binary_game(min_length, max_length, one_group, zero_group):
    dp = [0]*(max_length+1)
    dp[one_group] = 1
    dp[zero_group] += 1
    for i in range(min(one_group, zero_group)+1, max_length+1):
        if i - one_group >= 0:
            dp[i] += dp[i-one_group]
        if i - zero_group >= 0:
            dp[i] += dp[i-zero_group]
    return sum(dp[min_length:max_length+1]) % (10**9+7)
print(binary_game(min_length, max_length, one_group, zero_group))

arr = [1,2,3,2]
def efficient_team(arr):
    if len(arr) % 2 != 0:
        return -1
    total_sum = sum(arr)
    n = len(arr)
    if total_sum * 2 % n != 0:
        return -1
    sum_of_pair = total_sum * 2 // n
    sum_of_effiency = 0
    candidates = {}
    for num in arr:
        if num > sum_of_pair:
            return -1
        complement = sum_of_pair - num
        if complement in candidates:
            candidates[complement] -= 1
            sum_of_effiency += num * complement
        else:
            candidates[num] = candidates.get(num, 0) + 1
    for value in candidates.values():
        if value != 0:
            return -1
    return sum_of_effiency
print(efficient_team(arr))