class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i, j = len(a)-1, len(b)-1
        res = ''
        carry = 0
        while i >=0 or j >= 0:
            if i >= 0: 
                carry += int(a[i])
            if j >= 0: 
                carry += int(b[j])
            i, j = i-1, j-1
            res = str(carry % 2) + res
            carry = 1 if carry > 1 else 0
        if carry == 1:
            res = '1' + res
        return res

if __name__ == "__main__":
    a = "11"
    b = "1"
    assert "100" == Solution().addBinary(a, b)

    a = "1010"
    b = "1011"
    assert "10101" == Solution().addBinary(a, b)