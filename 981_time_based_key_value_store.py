from sortedcontainers import SortedList


class TimeMap:

    def __init__(self):
        self.data = {}
        self.value_dict = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        # no element:
        if key not in self.data:
            self.data[key] = SortedList()
        self.data[key].add(timestamp)
        self.value_dict[(key, timestamp)] = value

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.data or timestamp < self.data[key][0]:
            return ""
        index = self.data[key].bisect_right(timestamp)-1
        return self.value_dict[(key, self.data[key][index])]

timeMap = TimeMap()
timeMap.set("foo", "bar", 1)
timeMap.get("foo", 1)
timeMap.get("foo", 3)
timeMap.set("foo", "bar2", 4)
timeMap.get("foo", 4)
timeMap.get("foo", 5)
