class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        
        l = 0
        r = 0

        longest = 0
        curr = 0

        # Should probably use two pointers

        included = [0] * 127

        while r < len(s):
            
            rchar = ord(s[r])

            if included[rchar] == 0:
                included[rchar] = 1
                curr += 1
                longest = max(longest, curr)
            else:
                lchar = ord(s[l])
                while rchar != lchar and l<r:
                    included[lchar] = 0
                    curr -= 1
                    l += 1
                    lchar = ord(s[l])
                l += 1
            
            r += 1
        return longest