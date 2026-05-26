class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0

        maxLen = 0
        counts = {}

        # We basically want to keep track of the size of the window and how many we would need to replace
        # And we want that to be less than k, i.e., (window_size - largest_sequence) <= k

        for r in range(len(s)):
            counts[s[r]] = 1 + counts.get(s[r], 0)
            while ((r-l+1) - max(counts.values())) > k: # Here we have to narrow down the window size
                counts[s[l]] -= 1
                l += 1
            maxLen = max(maxLen, r-l+1)
        return maxLen
            
