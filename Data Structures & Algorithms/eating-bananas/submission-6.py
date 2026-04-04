class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # brute force, start by k = 1 and go up until you can actually finish the bananas

        # how can we increase this? can we bound it?
        # I think it can be bounded, one case is if the length of the piles is equal to the h, then simply return the largest element in the list

        if h == len(piles): # Simplest case
            return max(piles)
        
        # If h > len(piles) then we can in theory have a value lower than the maximum (i.e., we have bounded the value)

        # Use binary search over search space [1, max(piles)]
        hi, lo = max(piles), 1

        while hi > lo:
            # Iterate through and check
            batches = 0
            mid = (hi+lo)//2
            for p in piles:
                val = math.ceil(p/mid)
                batches += val
                
            if batches > h:
                lo = mid + 1
            else:
                hi = mid
            
        return hi