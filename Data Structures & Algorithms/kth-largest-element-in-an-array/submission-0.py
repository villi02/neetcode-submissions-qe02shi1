class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Simply use a maxHeap of size k?

        maxHeap = []
        for val in nums:
            heapq.heappush(maxHeap, val)
            if len(maxHeap) > k:
                heapq.heappop(maxHeap)
        
        

        return maxHeap[0]