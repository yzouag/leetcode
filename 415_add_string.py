class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        i, j = len(num1)-1, len(num2)-1
        res = ''
        carry = 0
        while i >= 0 or j >= 0:
            if i >= 0:
                carry += ord(num1[i]) - ord('0')
            if j >= 0:
                carry += ord(num2[j]) - ord('0')
            i, j = i-1, j-1
            res = str(carry % 10) + res
            carry = 0 if carry < 10 else 1
        if carry == 1:
            res = '1' + res
        return res

if __name__ == "__main__":
    num1 = "11"
    num2 = "123"
    assert Solution().addStrings(num1, num2) == "134"
    
    num1 = "456"
    num2 = "77"
    assert Solution().addStrings(num1, num2) == "533"

    num1 = "0"
    num2 = "0"
    assert Solution().addStrings(num1, num2) == "0"