class MinStack:

    def __init__(self):
        self.values = []
        self.smallest_indexes = [] # basically going to keep track of these

    def push(self, val: int) -> None:
        self.values.append(val)
        if not self.smallest_indexes:
            self.smallest_indexes.append(0)
        elif val < self.values[self.smallest_indexes[-1]]:
            self.smallest_indexes.append(len(self.values) - 1)
        else:
            existing_smallest = self.smallest_indexes[-1]
            self.smallest_indexes.append(existing_smallest)

    def pop(self) -> None:
        del self.values[-1]
        del self.smallest_indexes[-1]
        

    def top(self) -> int:
        return self.values[-1]

    def getMin(self) -> int:
        return self.values[self.smallest_indexes[-1]]
        
