from typing import List
def numSimilarGroups(strs: List[str]) -> int:
    def isSimilar(s1, s2) -> bool:
        sims = 0
        for i in range(len(s1)):
            if s1[i] == s2[i]:
                sims += 1
        return sims == len(s1)-2 or sims == len(s1)

    n = len(strs)
    groups = {i: i for i in range(n)}

    def find(i):
        if groups[i] == i:
            return i
        groups[i] = find(groups[i])
        return groups[i]

    for i in range(n):
        for j in range(i+1, n):
            if isSimilar(strs[i], strs[j]):
                p_i = find(i)
                p_j = find(j)
                if p_i != p_j:
                    groups[p_j] = p_i

    counts = 0
    for i in range(n):
        if groups[i] == i:
            counts += 1
    return counts

strs = ["tars","rats","arts","star"]
print(numSimilarGroups(strs))
# Output: 2

strs = ["omv","ovm"]
print(numSimilarGroups(strs))
# Output: 1

strs = ["kccomwcgcs","socgcmcwkc","sgckwcmcoc","coswcmcgkc","cowkccmsgc","cosgmccwkc","sgmkwcccoc","coswmccgkc","kowcccmsgc","kgcomwcccs"]
print(numSimilarGroups(strs))
# Output: 5
