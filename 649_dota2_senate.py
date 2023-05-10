def predictPartyVictory(senate: str) -> str:
    num_r = 0
    num_d = 0
    while len(senate) > num_r and len(senate) > num_d:
        res = ''
        for senator in senate:
            if senator == 'R':
                if num_d > 0:
                    num_d -= 1
                else:
                    num_r += 1
                    res += 'R'
            else:
                if num_r > 0:
                    num_r -= 1
                else:
                    num_d += 1
                    res += 'D'
        senate = res
    
    if senate[0] == 'R':
        return 'Radiant'
    else:
        return 'Dire'
    

senate = "RD"
print(predictPartyVictory(senate))
# Output: "Radiant"

senate = "RDD"
print(predictPartyVictory(senate))
# Output: "Dire"

senate = "RRDDD"
print(predictPartyVictory(senate))
# Output: "Radiant"

senate = "RDR"
print(predictPartyVictory(senate))
# Output: "Radiant"