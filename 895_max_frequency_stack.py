from collections import defaultdict
class FreqStack:

    def __init__(self):
        self.maxFreq = 0
        self.freq = defaultdict(int) # num: frequency
        self.group = defaultdict(list) # frequncy: [stack of nums of that frequency]

    def push(self, val: int) -> None:
        self.freq[val] += 1
        if self.freq[val] > self.maxFreq: # if now this val has the largest frequency, update the max frequency
            self.maxFreq = self.freq[val]
        self.group[self.freq[val]].append(val) # add that number to frequency map
        # note that like push(3) for 3 times
        # self.group will be {1:[3], 2:[3], 3:[3]}

    def pop(self) -> int:
        res = self.group[self.maxFreq].pop()
        self.freq[res] -= 1
        if len(self.group[self.maxFreq]) == 0:
            self.maxFreq -= 1
        return res
        


# Your FreqStack object will be instantiated and called as such:
freqStack = FreqStack()
freqStack.push(5)  # The stack is [5]
freqStack.push(7)  # The stack is [5,7]
freqStack.push(5)  # The stack is [5,7,5]
freqStack.push(7)  # The stack is [5,7,5,7]
freqStack.push(4)  # The stack is [5,7,5,7,4]
freqStack.push(5)  # The stack is [5,7,5,7,4,5]
freqStack.pop()    # return 5, as 5 is the most frequent. The stack becomes [5,7,5,7,4].
freqStack.pop()    # return 7, as 5 and 7 is the most frequent, but 7 is closest to the top. The stack becomes [5,7,5,4].
freqStack.pop()    # return 5, as 5 is the most frequent. The stack becomes [5,7,4].
freqStack.pop()    # return 4, as 4, 5 and 7 is the most frequent, but 4 is closest to the top. The stack becomes [5,7].