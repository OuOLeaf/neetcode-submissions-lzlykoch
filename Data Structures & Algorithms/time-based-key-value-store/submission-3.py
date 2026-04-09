class TimeMap:
    def __init__(self):
        self.KVdict = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.KVdict:
            self.KVdict[key] = {}
        self.KVdict[key][timestamp] = value

    def get(self, key: str, timestamp: int) -> str:
        if self.KVdict.get(key):
            res = list(self.KVdict.get(key).keys())
            value = list(self.KVdict.get(key).values())
            l = 0
            r = len(res) - 1
            ans = -1
            while(l <= r):
                mid = (l + r) // 2
                mr = res[mid]
                if ans <= mid and res[mid] <= timestamp:
                    ans = mid
                if timestamp >= mr:
                    l = mid + 1
                else:
                    r = mid - 1
            print(ans)
            return value[ans] if ans != -1 else ""
        else:
            return ""
        