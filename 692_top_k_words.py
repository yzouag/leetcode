from typing import List
from collections import Counter
import heapq

def topKFrequent(words: List[str], k: int) -> List[str]:
    # Freqs = Counter(words)
    # # here we must use nsmallest, because we want to sort in alphabetic order
    # # "a" < "b" so we want "a" which is smaller, but we also want large frequencies
    # # so we must use -Freqs
    # return heapq.nsmallest(k, Freqs, key=lambda w:(-Freqs[w], w))

    # a more orthodox way
    class node:
        def __init__(self, word, freqs) -> None:
            self.word = word
            self.freqs = freqs
        def __lt__(self, other) -> bool:
            if self.freqs == other.freqs:
                return self.word > other.word
            return self.freqs < other.freqs
    
    counts = {}
    for word in words:
        counts[word] = counts.get(word, 0) + 1
    topK = []
    for word, freqs in counts.items():
        if len(topK) < k:
            heapq.heappush(topK, node(word, freqs))
        else:
            heapq.heappushpop(topK, node(word, freqs))
    res = []
    for _ in range(k):
        res.insert(0, heapq.heappop(topK).word)
    return res
            

words = ["i","love","leetcode","i","love","coding"]
k = 2
print(topKFrequent(words, k))
# Output: ["i","love"]

words = ["the","day","is","sunny","the","the","the","sunny","is","is"]
k = 4
print(topKFrequent(words, k))
# Output: ["the","is","sunny","day"]