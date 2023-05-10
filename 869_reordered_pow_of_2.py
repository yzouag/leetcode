import itertools
def reorderedPowerOf2(n: int) -> bool:
    return any(cand[0] != '0' and bin(int("".join(cand))).count('1') == 1
                   for cand in itertools.permutations(str(n)))


n = 1
print(reorderedPowerOf2(n))
# Output: true

n = 10
print(reorderedPowerOf2(n))
# Output: false