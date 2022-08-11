class Solution:
    def convert(self, s: str, numRows: int) -> str:
        temp = [""] * numRows
        direction = 1
        currentPos = 0
        for i in range(len(s)):
            temp[currentPos] += s[i]
            if currentPos == 0:
                direction = 1
            if currentPos == numRows-1:
                direction = -1
            currentPos += direction
        result = ""
        for i in range(numRows):
            result += temp[i]
        return result

if __name__ == "__main__":
    s = "PAYPALISHIRING"
    numRows = 3
    assert "PAHNAPLSIIGYIR" == Solution().convert(s, numRows)

    s = "PAYPALISHIRING"
    numRows = 4
    assert "PINALSIGYAHRPI" == Solution().convert(s, numRows)

    s = "A"
    numRows = 1
    assert "A" == Solution().convert(s, numRows)