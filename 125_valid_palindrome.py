def isPalindrome(s: str) -> bool:
    processed_s = ""
    for w in s:
        if w.isalnum():
            processed_s += w.lower()

    l, r = 0, len(processed_s)-1
    while l <= r:
        if processed_s[l] != processed_s[r]:
            return False
        l += 1
        r -= 1
    return True

s = "race a car"
print(isPalindrome(s))
# Output: false

s = "A man, a plan, a canal: Panama"
print(isPalindrome(s))
# Output: true

s = " "
print(isPalindrome(s))
# Output: true