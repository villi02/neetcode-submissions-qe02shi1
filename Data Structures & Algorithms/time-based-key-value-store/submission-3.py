class TimeMap:

    def __init__(self):
        self.mappings = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.mappings:
            self.mappings[key] = {}
            self.mappings[key][timestamp] = value
        else:
            self.mappings[key][timestamp] = value

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.mappings:
            return ""
        stamps = list(self.mappings[key].keys())
        res = ""
        # Binary search
        l, r = 0, len(stamps)-1
        while l <= r:
            mid = (l+r)//2
            if stamps[mid] <= timestamp:
                res = self.mappings[key][stamps[mid]]
                l = mid + 1
            else:
                r = mid -1
                

        return res

    
        
