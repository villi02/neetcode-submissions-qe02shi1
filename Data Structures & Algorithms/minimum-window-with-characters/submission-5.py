class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Maybe just keep track of counts and when all are found, then simply close shrink the window

        if len(s) < len(t):
            return ""

        tracker = {}
        freq = {}

        l, r = 0,0
        satisfied = {}
        smallest = len(s)+1
        res = [l,r]

        for char in t:
            if char in tracker:
                freq[char] += 1
            else:
                freq[char] = 1
                tracker[char] = 0
        

        foundWindow = False

        while r < len(s):
            if s[r] in tracker:
                tracker[s[r]] += 1
                if tracker[s[r]] >= freq[s[r]]:
                    satisfied[s[r]] = True
            
            while len(satisfied) == len(freq): # now we shrink the window
                foundWindow = True
                d = r - l+1
                if d < smallest:
                    res = [l, r]
                    smallest = d
                if s[l] in tracker:
                    tracker[s[l]] -= 1
                    if tracker[s[l]] < freq[s[l]]:
                        del satisfied[s[l]]
                l += 1
            r += 1

        return s[res[0]: res[1]+1] if foundWindow else ""