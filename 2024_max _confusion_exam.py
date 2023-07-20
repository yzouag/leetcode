# sliding window

# solution:
# for a subarray, if min(num_T, num_F) <= k, then length of this subarray is the max confusion
# build a sliding window (always increase the size) and a counter for T,F
# if valid, then max_res = len(current_window)
def maxConsecutiveAnswers(answerKey: str, k: int) -> int:
    i, j = 0, 0
    counter = [0, 0] # [T, F]
    res = 0

    while j < len(answerKey):
        if answerKey[j] == 'T': # put next question into sliding window
            counter[0] += 1
        else:
            counter[1] += 1
        
        if min(counter) <= k: # if current window is valid
            # expand window 1 more
            j += 1
            res = j - i # since we are expanding the window, res must be improved
        else: # current window not valid
            # move the window to right for 1 position
            # so we decrease the counter
            if answerKey[i] == 'T':
                counter[0] -= 1
            else:
                counter[1] -= 1
            i += 1
            j += 1

    return res

answerKey = "TTFF"
k = 2
print(maxConsecutiveAnswers(answerKey, k))
# Output: 4

answerKey = "TFFT"
k = 1
print(maxConsecutiveAnswers(answerKey, k))
# Output: 3

answerKey = "TTFTTFTT"
k = 1
print(maxConsecutiveAnswers(answerKey, k))
# Output: 5