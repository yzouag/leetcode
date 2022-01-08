class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window = [0] * 26
        target = [0] * 26
        window_size = len(s1)
        for c in s1:
            target[ord(c) - ord('a')] += 1
        
        for index, character in enumerate(s2):
            window[ord(character) - ord('a')] += 1
            if index > window_size - 1:
                window[ord(s2[index-window_size])-ord('a')] -= 1
            if window == target:
                return True
        return False
                

if __name__ == "__main__":
    s1 = 'ab'
    s2 = 'eidbaooo'
    s3 = 'eidboaoo'

    assert Solution().checkInclusion(s1, s2) == True
    assert Solution().checkInclusion(s1, s3) == False