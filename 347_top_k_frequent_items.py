from typing import List
from collections import defaultdict
import heapq
import random
def topKFrequent(nums: List[int], k: int) -> List[int]:
    # return list(map(lambda x: x[0], Counter(nums).most_common(k)))
    counts = defaultdict(int)
    for num in nums:
        counts[num] += 1
    
    # 1. using heap O(klogk)
    # res = heapq.nlargest(k, counts.items(), key=lambda x:x[1])
    # return list(map(lambda x: x[0], res))

    # 2. using bucket sort
    # freqs = [[] for _ in range(len(nums) + 1)]
    # for num, frequency in counts.items():
    #     freqs[frequency].append(num)

    # res = []
    # for i in range(len(nums), -1, -1):
    #     res.extend(freqs[i])
    #     if len(res) == k:
    #         return res

    # 3. using quicksort
    unique = list(counts.keys())
    def partition(left, right, pivot_index) -> int:
        pivot_frequency = counts[unique[pivot_index]]
        # 1. move pivot to end
        unique[pivot_index], unique[right] = unique[right], unique[pivot_index]  
        
        # 2. move all less frequent elements to the left
        store_index = left
        for i in range(left, right):
            if counts[unique[i]] < pivot_frequency:
                unique[store_index], unique[i] = unique[i], unique[store_index]
                store_index += 1

        # 3. move pivot to its final place
        unique[right], unique[store_index] = unique[store_index], unique[right]  
        
        return store_index
    
    def quickselect(left, right, k_smallest) -> None:
        """
        Sort a list within left..right till kth less frequent element
        takes its place. 
        """
        # base case: the list contains only one element
        if left == right: 
            return
        
        # select a random pivot_index
        pivot_index = random.randint(left, right)     
                        
        # find the pivot position in a sorted list   
        pivot_index = partition(left, right, pivot_index)
        
        # if the pivot is in its final sorted position
        if k_smallest == pivot_index:
                return 
        # go left
        elif k_smallest < pivot_index:
            quickselect(left, pivot_index - 1, k_smallest)
        # go right
        else:
            quickselect(pivot_index + 1, right, k_smallest)
        
    n = len(unique) 
    # kth top frequent element is (n - k)th less frequent.
    # Do a partial sort: from less frequent to the most frequent, till
    # (n - k)th less frequent element takes its place (n - k) in a sorted array. 
    # All element on the left are less frequent.
    # All the elements on the right are more frequent.  
    quickselect(0, n - 1, n - k)
    # Return top k frequent elements
    return unique[n - k:]

nums = [1,1,1,2,2,3]
k = 2
print(topKFrequent(nums, k))
# Output: [1,2]

nums = [1]
k = 1
print(topKFrequent(nums, k))
# Output: [1]