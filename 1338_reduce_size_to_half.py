from typing import List
from collections import Counter
def minSetSize(arr: List[int]) -> int:
    n = len(arr)

    num_freqs = Counter(arr)
    freqs_sorted = sorted(num_freqs.values(), reverse=True)

    total_removed = 0
    for i, num in enumerate(freqs_sorted):
        if num + total_removed >= 0.5*n:
            return i+1
        total_removed += num
    return 0

arr = [3,3,3,3,5,5,5,2,2,7]
print(minSetSize(arr))
# Output: 2

arr = [7,7,7,7,7,7]
print(minSetSize(arr))
# Output: 1