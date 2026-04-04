class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if not s:
            return 0

        # We could make an array with a value mapped to each character in the alphabet, and then just have a sliding window, where it checks the front against the array, if the value is 1, then move the back pointer
        lo, hi = 0, 0

        dup = [False] * 150

        maxLen = 0

        while hi < len(s):
            loAscii = ord(s[lo])
            hiAscii = ord(s[hi])

            loIndx = loAscii - 97
            hiIndex = hiAscii - 97

            if dup[hiIndex]: # Here we have found a duplicate, thus move lo until no duplicate exists
                while dup[hiIndex]:
                    loAscii = ord(s[lo])
                    loIndx = loAscii - 97
                    dup[loIndx] = False
                    lo += 1
            
            dup[hiIndex] = True
        
            hi += 1

            maxLen = max(maxLen, hi-lo)
        return maxLen