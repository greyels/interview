class TimeMap:

    def __init__(self):
        self.map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.map.keys():
            self.map[key] = [(timestamp, value)]
        else:
            self.map[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.map.keys():
            return ""
        else:
            return self.search(key, timestamp)

    def search(self, key: str, timestamp: int) -> str:
        tlst = self.map[key]
        left = 0
        right = len(tlst) - 1
        prev = ""
        while right >= left:
            mid = (right + left) // 2
            if tlst[mid][0] == timestamp:
                return tlst[mid][1]
            elif tlst[mid][0] > timestamp:
                right = mid - 1
            elif tlst[mid][0] < timestamp:
                left = mid + 1
                prev = tlst[mid][1]
        return prev

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
