class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        str_x = str(x)
        for i in range(len(str_x)//2):
            if str_x[i] != str_x[-(i+1)]:
                return False
        return True

if __name__ == "__main__":
    x = 121
    assert True == Solution().isPalindrome(x)

    x = -121
    assert False == Solution().isPalindrome(x)

    x = 10
    assert False == Solution().isPalindrome(x)