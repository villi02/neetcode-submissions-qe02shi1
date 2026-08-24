class TimeMap:

    def __init__(self):
        self.mappings = {} # Key is the key given, then the return value is a list

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.mappings:
            self.mappings[key] = {}
            self.mappings[key][timestamp] = value
        else:
            self.mappings[key][timestamp] = value

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.mappings:
            return ""
        else:
            if timestamp in self.mappings[key]:
                return self.mappings[key][timestamp]
            else: # here we need logic to find the highest valid key
                validStamps = [stamp for stamp in self.mappings[key].keys() if stamp <= timestamp]
                if not validStamps:
                    return ""
                maxStamp = max(validStamps)
                return self.mappings[key][maxStamp]

    
        
