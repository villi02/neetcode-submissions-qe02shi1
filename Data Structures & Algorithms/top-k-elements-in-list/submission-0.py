class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # Make n buckets
        count = {}

        for n in nums:
            count[n] = count.get(n, 0) + 1
            
        # Now adding to the buckers
        buckets = [[] for _ in range(len(nums) + 1)]
        for key, val in count.items():
            buckets[val].append(key)
        
        res = []
        for i in range(len(buckets) - 1, 0, -1):
            for vals in buckets[i]:
                res.append(vals)
                if len(res) == k:
                    return res
        