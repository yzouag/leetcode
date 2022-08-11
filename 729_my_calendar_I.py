# balanced tree will have a logN insertion time
# when insert, check the range
from sortedcontainers import SortedList
class MyCalendar:

    def __init__(self):
        self.queue = SortedList()

    def book(self, start: int, end: int) -> bool:
        prev = self.queue.bisect_left((start, end))
        next = self.queue.bisect_right((start, end))
        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)