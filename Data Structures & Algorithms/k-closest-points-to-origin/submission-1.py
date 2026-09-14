class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def distance(point):
            x,y = point[0], point[1]
            return x**2 + y**2
        
        maxHeap = []

        for x, y in points:
            dist = distance([x,y])

            heapq.heappush_max(maxHeap, [dist, x,y])
            if len(maxHeap) > k:
                heapq.heappop_max(maxHeap)
            
        res = []
        while maxHeap:
            dist, x, y = heapq.heappop_max(maxHeap)
            res.append([x,y])

        return res