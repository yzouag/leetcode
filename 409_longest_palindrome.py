def longestPalindrome(s: str) -> int:
    single_letter = set()
    pair = 0
    for letter in s:
        if letter not in single_letter:
            single_letter.add(letter)
        else:
            single_letter.remove(letter)
            pair += 1
    if single_letter:
        return 2*pair + 1
    else:
        return 2*pair
    

s = "abccccdd"
print(longestPalindrome(s))
# Output: 7

s = "a"
print(longestPalindrome(s))
# Output: 1