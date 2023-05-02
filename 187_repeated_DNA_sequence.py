from typing import List
from collections import defaultdict

# using the Rabin-Karp method
# key idea: using rolling hash


def findRepeatedDnaSequences(s: str) -> List[str]:
    if len(s) < 10:
        return []
    
    mapping = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
    table = defaultdict(int)
    
    L = 10
    hash_value = 0
    for i in range(L):
        hash_value += mapping[s[i]] * 5

s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
# Output: ["AAAAACCCCC","CCCCCAAAAA"]

s = "AAAAAAAAAAAAA"
# Output: ["AAAAAAAAAA"]