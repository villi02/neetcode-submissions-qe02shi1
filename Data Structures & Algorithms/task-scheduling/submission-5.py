class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Need heap and queue

        queue = deque()
        maxHeap = []

        freq = {}

        # Find frequencies
        for task in tasks:
            if task not in freq:
                freq[task] = 1
            else:
                freq[task] += 1
        
        for task, frequency in freq.items():
            heapq.heappush_max(maxHeap, (frequency, task))
        
        # Saving in queue (remaining, task, time when free)
        time = 0
        while maxHeap or queue:
            
            while queue and queue[0][2] <= time:
                remain, task, _ = queue.popleft()
                heapq.heappush_max(maxHeap, (remain, task))
            
            if maxHeap:
                remaining, task = heapq.heappop_max(maxHeap)
                if remaining -1 > 0:
                    queue.append((remaining-1, task, time+n+1))
            
            
            time += 1
        
        return time