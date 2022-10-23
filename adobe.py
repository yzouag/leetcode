import bisect
from collections import defaultdict
import heapq
from typing import List


def substring_reversal(word: str, k: int) -> str:
    for i in range(len(word)-k+1):
        reverse_str = "".join(reversed(word[i:i+k]))
        if word[i:i+k] > reverse_str:
            return word[:i] + reverse_str + word[i+k:]
    return word

word = "abadc"
k = 2
print(substring_reversal(word, k))
# Output: "aabcd"

def binge_watching(n: int, durations: List[int]) -> int:
    durations.sort()
    start, end = 0, len(durations)-1
    total = 0
    while start < end:
        if durations[start]+durations[end] < 3:
            total += 1
            start += 1
            end -= 1
        else:
            total += 1
            end -= 1
    if start == end:
        total += 1
    return total

n = 5
# durations = [1.90, 1.04, 1.25, 2.5, 1.75]
durations = [2,2,2,2,2]
print(binge_watching(n, durations))
# Output: 3

def similar_password(password: str) -> int:
    n = len(password)
    if n % 2 == 1:
        return -1
    vowels = set(["a", "e", "i", "o", "u"])
    num_vowels = 0
    consonants = []
    for c in password:
        if c in vowels:
            num_vowels += 1
        else:
            consonants.append(c)
    
    if num_vowels > n//2:
        return num_vowels - n//2
    if num_vowels == n//2:
        return 0

    operations = []
    for consonant in consonants:
        operations.append(min([abs(ord(consonant)-ord(x)) for x in vowels]))
    return sum(heapq.nsmallest(n//2-num_vowels, operations))

password = "haaadddscpck"
print(similar_password(password))
# Output: 1

def smash_the_bricks(bigHits: int, newtons: List[int]) -> List[int]:
    if len(newtons) <= bigHits:
        return [[len(newtons)], list(range(1, len(newtons)+1)), []]
    newtons_with_index = list(zip(newtons, list(range(1, len(newtons)+1))))
    
    max_heap = []
    big_list = []
    small_list = []
    cost = 0
    for i in range(bigHits):
        heapq.heappush(max_heap, newtons_with_index[i])
    for i in range(bigHits, len(newtons)):
        newton, index = heapq.heappushpop(max_heap, newtons_with_index[i])
        cost += newton
        small_list.append(index)
    for _, index in max_heap:
        big_list.append(index)
    small_list.sort()
    big_list.sort()
    return [[cost+bigHits], big_list, small_list]

bigHits = 4
newtons = [3,2,5,4,6,7,9]
print(smash_the_bricks(bigHits, newtons))
# Output: [[13], [3,5,6,7], [1,2,4]]

def match_outcome(numSeq: List[int]) -> int:
    directions = [[0, 1], [len(numSeq)-1, -1]]
    state = 0
    first = second = 0
    for i in range(len(numSeq)):
        index, direction = directions[state]
        directions[state][0] += direction
        num = numSeq[index]
        if num % 2 == 0:
            state = (state + 1) % 2
        if i % 2 == 0:
            first += num
        else:
            second += num
    return first - second
    
numSeq = [3,6,2,3,5]
print(match_outcome(numSeq))
# Output: 1

def sum_in_range(arr: List[int], l: int, r: int) -> int:
    arr.sort()
    res = 0
    for i in range(len(arr)-1):
        left = arr[i]
        lower = l - left
        upper = r - left
        if lower > arr[i+1:][-1] or upper < arr[i+1:][0]:
            continue
        lower_index = bisect.bisect_left(arr[i+1:], lower) + i + 1
        upper_index = bisect.bisect_left(arr[i+1:], upper) + i + 1
        res += min(upper_index, len(arr)-1) - lower_index + 1
    return res

    
arr = [2,3,4,5]
l = 5
r = 7
print(sum_in_range(arr, l, r))
# Output: 4

def freelancing_platform(numProjects: int, projectID: List[int], bid: List[int]) -> int:
    project_bids = {}
    for i in range(len(projectID)):
        if projectID[i] not in project_bids:
            project_bids[projectID[i]] = bid[i]
        else:
            project_bids[projectID[i]] = min(project_bids[projectID[i]], bid[i])
    if len(project_bids) < numProjects:
        return -1
    return sum(project_bids.values())

numProjects = 3
projectID = [2,0,1,2]
bid = [8,7,6,9]
print(freelancing_platform(numProjects, projectID, bid))
# Output: 21

numProjects = 4
projectID = [2,0,1,2]
bid = [8,7,6,9]
print(freelancing_platform(numProjects, projectID, bid))
# Output: -1