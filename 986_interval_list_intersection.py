from typing import List

class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        """
        i, j = 0, 0
        res = []
        while i < len(firstList) and j < len(secondList):
            start_i, end_i = firstList[i]
            start_j, end_j = secondList[j]
            if end_i < start_j:
                i += 1
                continue
            if end_j < start_i:
                j += 1
                continue
            if start_i < start_j:
                if end_i < end_j:
                    res.append([start_j, end_i])
                    i += 1
                    continue
                else:
                    res.append([start_j, end_j])
                    j += 1
                    continue
            else:
                if end_j < end_i:
                    res.append([start_i, end_j])
                    j += 1
                    continue
                else:
                    res.append([start_i, end_i])
                    i += 1
                    continue
        return res
        """
        i,j = 0,0
        res = []
        while i < len(firstList) and j < len(secondList):
            curr = [max(firstList[i][0], secondList[j][0]), min(firstList[i][1], secondList[j][1])]

            if curr[0] <= curr[1]:
                res.append(curr)
            if firstList[i][1] < secondList[j][1]:
                i += 1
            else:
                j += 1
        return res


if __name__ == "__main__":
    firstList = [[0,2],[5,10],[13,23],[24,25]]
    secondList = [[1,5],[8,12],[15,24],[25,26]]

    assert [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]] == Solution().intervalIntersection(firstList, secondList)

    firstList = [[1,3],[5,9]]
    secondList = []

    assert [] == Solution().intervalIntersection(firstList, secondList)