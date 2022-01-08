"""
indext    0    1    2    3   4   5   6   7
string    a    c    b    d   b   a   c   d
          ^                  ^
          |                  |
		left               right
		seen = {a : 0, c : 1, b : 2, d: 3} 
		# case 1: seen[b] = 2, current window  is s[0:4] , 
		#        b is inside current window, seen[b] = 2 > left = 0. Move left pointer to seen[b] + 1 = 3
		seen = {a : 0, c : 1, b : 4, d: 3} 
indext    0    1    2    3   4   5   6   7
string    a    c    b    d   b   a   c   d
						 ^   ^
					     |   |
				      left  right		
indext    0    1    2    3   4   5   6   7
string    a    c    b    d   b   a   c   d
					     ^       ^
					     |       |
				       left    right		
		# case 2: seen[a] = 0,which means a not in current window s[3:5] , since seen[a] = 0 < left = 3 
		# we can keep moving right pointer.
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        max_length = 0
        seen = {}
        for right, c in enumerate(s):
            # if the pointing character is already in the window, update the window's left to exclude the existing character 
            if c in seen and seen[c] >= left:
                left = seen[c] + 1
            # update the seen dictionary
            seen[c] = right
            max_length = max(max_length, right-left+1)
        return max_length


if __name__ == "__main__":
    s = "bbba"
    print(Solution().lengthOfLongestSubstring(s))