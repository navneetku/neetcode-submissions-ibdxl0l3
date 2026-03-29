class TimeMap:

    def __init__(self):
        self.value = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.value:
            self.value[key] = []
        self.value[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res = ''
        list_values = self.value.get(key, [])
        l, r = 0, len(list_values) - 1

        while l<=r:
            m = (l + r)//2
            if list_values[m][1] <= timestamp:
                res = list_values[m][0]
                l = m + 1
            else:
                r = m - 1
        return res

# Time Complexity: O(logn)
# Space Complexity: O(m*n)
