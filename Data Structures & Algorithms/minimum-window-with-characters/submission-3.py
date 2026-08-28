class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        
        """
        res = [0, len(s)-1]

        tracker = {}
        # Maybe also keep track of the indexes with a queue
        queue = deque()

        for char in t:
            tracker[char] = False
        
        l, r = 0, 1

        while r < len(s):
            
            if s[r] in tracker: # Now logic for moving if needed
                if (tracker[s[r]]) and (s[l] == s[r]): # now we can safely move
                    newl = queue.popleft()
                    l = newl
                    


        return s[res[0]: res[1]+1]
        """
        # Maybe just keep track of counts and when all are found, then simply close shrink the window

        tracker = {}
        freq = {}

        l, r = 0,0
        satisfied = {}
        smallest = len(s)
        res = [l,r]

        for char in t:
            if char in tracker:
                freq[char] += 1
            else:
                freq[char] = 1
                tracker[char] = 0
            
        
        need = len(tracker)

        foundWindow = False

        while r < len(s):
            if s[r] in tracker:
                tracker[s[r]] += 1
                if tracker[s[r]] >= freq[s[r]]:
                    satisfied[s[r]] = True
            
            while len(satisfied) == len(freq): # now we shrink the window
                foundWindow = True
                d = r - l
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