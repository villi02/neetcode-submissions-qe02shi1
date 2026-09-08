class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Make one min-heap and one max-heap        
        
        if not stones:
            return 0

        heapq.heapify_max(stones)

        while len(stones) > 1:
            largest = heapq.heappop_max(stones)
            second = heapq.heappop_max(stones)

            diff = abs(largest - second)
            if diff > 0:
                heapq.heappush_max(stones, diff)
            if len(stones) == 0:
                return diff
            if len(stones) < 2:
                return stones[0]
        
        
        return stones[0]