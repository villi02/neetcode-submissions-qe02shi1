class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        time = 0

        counts = {}

        for char in tasks:
            if char not in counts:
                counts[char] = 1
            else:
                counts[char] += 1
        
        maxHeap = []

        for key, val in counts.items():
            heapq.heappush_max(maxHeap, (val,key))
        
        cooldown = deque()
        busy = {}

        while cooldown or maxHeap:
            
            while cooldown and cooldown[0][2] <= time:    
                newVal, newKey, _ = cooldown.popleft()
                heapq.heappush_max(maxHeap, (newVal, newKey))

            if maxHeap:
                val, key = heapq.heappop_max(maxHeap)
                val -= 1
                if val > 0:
                    cooldown.append((val, key, time+n+1))
            time += 1

        return time