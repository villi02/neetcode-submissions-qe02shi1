class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Maybe just have two pointers, of length s1, then keep counts of the variables inside s2 inside the window

        counts = {}

        for s in s1:
            counts[s] = 1 + counts.get(s, 0)
        
        l = 0

        for r in range(len(s2)):
            if (r-l +1) > len(s1):
                if s2[l] in counts:
                    counts[s2[l]] += 1
                l += 1
            if s2[r] in counts:
                counts[s2[r]] -= 1
            if max(counts.values()) == 0:
                return True
        return False
            
