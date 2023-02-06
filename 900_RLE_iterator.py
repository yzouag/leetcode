from typing import List
class RLEIterator:

    def __init__(self, encoding: List[int]):
        self.arr = encoding
        

    def next(self, n: int) -> int:
        while self.arr:
            if n > self.arr[0]:
                n -= self.arr[0]
                self.arr = self.arr[2:]
            else:
                self.arr[0] -= n
                return self.arr[1]
        return -1
        
rLEIterator = RLEIterator([3, 8, 0, 9, 2, 5]) # This maps to the sequence [8,8,8,5,5].
rLEIterator.next(2) # exhausts 2 terms of the sequence, returning 8. The remaining sequence is now [8, 5, 5].
rLEIterator.next(1) # exhausts 1 term of the sequence, returning 8. The remaining sequence is now [5, 5].
rLEIterator.next(1) # exhausts 1 term of the sequence, returning 5. The remaining sequence is now [5].
rLEIterator.next(2) # exhausts 2 terms, returning -1. This is because the first term exhausted was 5,
                    # but the second term did not exist. Since the last term exhausted does not exist, we return -1.