import bisect
from collections import defaultdict

class TimeMap:
    def __init__(self):
        self.data = defaultdict(lambda: [[], []])

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.data[key][0].append(timestamp)
        self.data[key][1].append(value)

    def get(self, key: str, timestamp: int) -> str:
        if len(self.data[key][0]) == 0 or self.data[key][0][0] > timestamp:
            return ""
        idx = bisect.bisect(self.data[key][0], timestamp)
        return self.data[key][1][idx-1]
        