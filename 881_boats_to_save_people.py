from typing import List
import bisect

def numRescueBoats(people: List[int], limit: int) -> int:
    # people.sort()
    # l, r = 0, len(people)-1

    # res = 0

    # while l <= r:
    #     if l == r:
    #         return res+1
    #     if people[l] + people[l+1] > limit:
    #         return res + (r-l+1)
        
    #     i = bisect.bisect_right(people, limit-people[l], l, r+1)

    #     res += r + 1 - i + 1 # index above i must not be paired with index >= l
    #     r = i-2
    #     l = l+1
    
    # return res

    # idea: greedy
    people.sort()
    i, j = 0, len(people) - 1
    ans = 0
    while i <= j:
        ans += 1
        if people[i] + people[j] <= limit:
            i += 1
        j -= 1
    return ans

people = [1,2]
limit = 3
print(numRescueBoats(people, limit))
# Output: 1

people = [3,2,2,1]
limit = 3
print(numRescueBoats(people, limit))
# Output: 3

people = [3,5,3,4]
limit = 5
print(numRescueBoats(people, limit))
# Output: 4

people = [3,2,3,2,2]
limit = 6
print(numRescueBoats(people, limit))
# Output: 3

people = [5,1,4,2]
limit = 6
print(numRescueBoats(people, limit))
# Output: 2
