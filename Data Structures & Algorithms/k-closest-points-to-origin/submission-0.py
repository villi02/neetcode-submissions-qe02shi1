class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def distance(point):
            x,y = point[0], point[1]
            return (x**2 + y**2)**0.5
        
        tot = len(points)
        points = points
        distances = [(distance(point),point) for point in points]

        heapq.heapify_max(distances)
        
        for _ in range(tot-k):
            heapq.heappop_max(distances)
        
        res = [dist[1] for dist in distances]

        return res