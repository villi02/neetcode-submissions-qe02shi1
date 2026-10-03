# We could in theory just keep a list sorted, then simply take the median from there, but thats not that efficients I think.
class MedianFinder:

    def __init__(self):
        self.Button = [] # max heap
        self.Top = [] # min heap
        heapq.heapify(self.Top)
        heapq.heapify(self.Button)

        self.len = 0

    def addNum(self, num: int) -> None:
        maxH = self.Top[0] if len(self.Top) else float("-infinity")

        if num < maxH:
            heapq.heappush_max(self.Button, num)
        else:
            heapq.heappush(self.Top, num)

        if abs(len(self.Button) - len(self.Top)) > 1:
            if len(self.Button) > len(self.Top):
                element = heapq.heappop_max(self.Button)
                heapq.heappush(self.Top, element)
            else:
                element = heapq.heappop(self.Top)
                heapq.heappush_max(self.Button, element)
            

    def findMedian(self) -> float:
        if (len(self.Button)+ len(self.Top)) % 2 == 0: # even number
            return (self.Button[0] + self.Top[0])/2
        else:
            return self.Button[0] if len(self.Button) > len(self.Top) else self.Top[0]
        