# cmax counts the maximum open parenthesis,
# which means the maximum number of unbalanced '(' that COULD be paired.
# cmin counts the minimum open parenthesis,
# which means the number of unbalanced '(' that MUST be paired.

# Too many ')' at any instant when parsing the string from the left
# At least one '(' at the end that doesn't have a matching ')'
# cmax only deals with 1. since it treats each * as '(', hence any time number of ')' exceeds max. possible '(', s is flagged as invalid.
# cmin only deals with 2. since it treats each * as ')' AND clips its own value at 0. Therefore, it doesn't care if there are two many ')' (saturated at 0) but if there are any '(' with no matching ')' at the end then it invalidates the string s.
# cmax and cmin are complementary as they deal with two scenarios that can invalidate a string.

def checkValidString(s: str) -> bool:
    max_open = 0 # at most `max_open` ')' required
    min_open = 0 # at least `min_open` ')' required
    for char in s:
        if char == '(': # both increases
            max_open += 1
            min_open += 1
        elif char == ')':
            max_open -= 1
            # now we have at most max_open left brackets, if it is negative means we cannot accept any more (
            if max_open < 0: 
                return False
            # concat is to 0, consider case *(, if it goes to 
            min_open = max(0, min_open-1)
        else:
            max_open += 1
            min_open = max(0, min_open-1)
    return min_open == 0

s = "()"
print(checkValidString(s)) 
# true

s = "(*)"
print(checkValidString(s)) 
# Output: true

s = "(*))"
print(checkValidString(s)) 
# Output: true

s = "*("
print(checkValidString(s))