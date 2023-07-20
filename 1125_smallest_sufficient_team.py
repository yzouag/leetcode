from typing import List
def smallestSufficientTeam(req_skills: List[str], people: List[List[str]]) -> List[int]:
    smallest = n = len(people)
    res = [i for i in range(n)]
    
    # create bit index for each skill
    mapping = {}
    for i, skill in enumerate(req_skills):
        mapping[skill] = i

    full_mask = 2**len(req_skills)-1
    
    people_included = []
    visited = set()

    def dfs(index: int, mask: int):
        nonlocal smallest, res
        if mask == full_mask:
            if smallest > len(people_included):
                smallest = len(people_included)
                res = people_included.copy()
        if index == n:
            return
        
        # if already visited 
        # if (index, mask) in visited:
        #     return 
        # visited.add((index, mask))
        
        # either ignore this person
        dfs(index+1, mask)

        # or include current person
        for skill in people[index]:
            mask |= 1 << mapping[skill]
        people_included.append(index)
        dfs(index+1, mask)
        people_included.pop()
    
    dfs(0, 0)
    return res


req_skills = ["java","nodejs","reactjs"]
people = [["java"],["nodejs"],["nodejs","reactjs"]]
print(smallestSufficientTeam(req_skills, people))
# Output: [0,2]

req_skills = ["algorithms","math","java","reactjs","csharp","aws"]
people = [["algorithms","math","java"],["algorithms","math","reactjs"],["java","csharp","aws"],["reactjs","csharp"],["csharp","math"],["aws","java"]]
print(smallestSufficientTeam(req_skills, people))
# Output: [1,2]

req_skills = ["mwobudvo","goczubcwnfze","yspbsez","pf","ey","hkq"]
people = [[],["mwobudvo"],["hkq"],["pf"],["pf"],["mwobudvo","pf"],[],["yspbsez"],[],["hkq"],[],[],["goczubcwnfze","pf","hkq"],["goczubcwnfze"],["hkq"],["mwobudvo"],[],["mwobudvo","pf"],["pf","ey"],["mwobudvo"],["hkq"],[],["pf"],["mwobudvo","yspbsez"],["mwobudvo","goczubcwnfze"],["goczubcwnfze","pf"],["goczubcwnfze"],["goczubcwnfze"],["mwobudvo"],["mwobudvo","goczubcwnfze"],[],["goczubcwnfze"],[],["goczubcwnfze"],["mwobudvo"],[],["hkq"],["yspbsez"],["mwobudvo"],["goczubcwnfze","ey"]]
print(smallestSufficientTeam(req_skills, people))
# Output: [12,23,39]
