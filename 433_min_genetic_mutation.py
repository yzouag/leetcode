from typing import List

def valid_mutate(g1: str, g2: str) -> bool:
    diff = 0
    for i in range(len(g1)):
        if g1[i] != g2[i]:
            diff += 1
        if diff > 1:
            return False
    return True

def minMutation(startGene: str, endGene: str, bank: List[str]) -> int:
    queue = []
    rest = []
    for gene in bank:
        if gene == startGene:
            continue
        if valid_mutate(startGene, gene):
            queue.append(gene)
        else:
            rest.append(gene)
    
    step = 1
    while queue:
        temp_queue = []
        for g1 in queue:
            if g1 == endGene:
                return step
            temp_rest = []
            for g2 in rest:
                if valid_mutate(g1, g2):
                    temp_queue.append(g2)
                else:
                    temp_rest.append(g2)
            rest = temp_rest
        queue = temp_queue
        step += 1
    
    return -1


startGene = "AACCGGTT"
endGene = "AACCGGTA"
bank = ["AACCGGTA"]
print(minMutation(startGene, endGene, bank))
# Output: 1

startGene = "AACCGGTT"
endGene = "AAACGGTA"
bank = ["AACCGGTA","AACCGCTA","AAACGGTA"]
print(minMutation(startGene, endGene, bank))
# Output: 2