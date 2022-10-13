from sortedcontainers import SortedDict


class MyCalendarThree:
    # method 1:
    # sweep line algorithm
    # use a dict or an array (here use dict because start and end are sparse)
    # for example:
    #  0  5    10   15  20  25  30  40  50  60
    # [0  +2  -1+2  -1  -1  +1  0   -1  +1  -2]
    def __init__(self):
        self.step = SortedDict()

    def book(self, start: int, end: int) -> int:
        self.step[start] = self.step.get(start, 0) + 1
        self.step[end] = self.step.get(end, 0) - 1
        cur, maximum = 0, 0
        for delta in self.step.values():
            cur += delta
            maximum = max(cur, maximum)
        return maximum


# Your MyCalendarThree object will be instantiated and called as such:
myCalendarThree = MyCalendarThree()
print(myCalendarThree.book(10, 20))
print(myCalendarThree.book(50, 60))
print(myCalendarThree.book(10, 40))
print(myCalendarThree.book(5, 15))
print(myCalendarThree.book(5, 10))
print(myCalendarThree.book(25, 55))
