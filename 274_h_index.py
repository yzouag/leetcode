from typing import List

def hIndex(citations: List[int]) -> int:
    # citations.sort()
    # res = 0
    # total_papers = len(citations)
    # for i, cites in enumerate(citations):
    #     res = max(res, min(cites, total_papers-i))
    # return res

    # idea: using counting sort
    # reason: know the input range, O(n) complexity
    n = len(citations)
    cite_counts = [0] * (n+1)
    # for cites greater than number of papers, treat them as cite_counts[n]
    for cite in citations:
        if cite > n:
            cite_counts[n] += 1
        else:
            cite_counts[cite] += 1
    
    counts = 0
    for i in range(n+1):
        counts += cite_counts[n-i]
        if counts >= n-i:
            return n-i
    return 0

citations = [3,0,6,1,5]
print(hIndex(citations))
# Output: 3

citations = [1,3,1]
print(hIndex(citations))
# Output: 1