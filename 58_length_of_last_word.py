def lengthOfLastWord(s: str) -> int:
    return len(s.strip().split(' ')[-1])

s = "Hello World"
print(lengthOfLastWord(s))
# Output: 5

s = "   fly me   to   the moon  "
print(lengthOfLastWord(s))
# Output: 4

s = "luffy is still joyboy"
print(lengthOfLastWord(s))
# Output: 6
