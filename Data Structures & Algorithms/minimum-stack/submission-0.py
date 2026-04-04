class MinStack:

    def __init__(self):
        self.minStack = []
        self.minIndex = []

    def push(self, val: int) -> None:
        self.minStack.append(val)
        if len(self.minIndex) > 0:
            currentMinIndex = self.minIndex[-1]
        else:
            currentMinIndex = 0
        
        newMinIndex = currentMinIndex
        if self.minStack[currentMinIndex] > val:
            newMinIndex = len(self.minStack) - 1
        self.minIndex.append(newMinIndex)

    def pop(self) -> None:
        del self.minStack[-1]
        del self.minIndex[-1]

    def top(self) -> int:
        return self.minStack[-1]

    def getMin(self) -> int:
        minIndex = self.minIndex[-1]
        minVal = self.minStack[minIndex]
        return minVal
