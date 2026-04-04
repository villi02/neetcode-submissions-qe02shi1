class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # We can use hashmaps here, to simply iterate through the words and count frequencies
        # But this would be O(n + m) complexity for space.
        # I think we can just make one array, where each element is a letter of the alphabet and then simply count
        # A Hashmap with frequencies does the same thing I think

        """
        freq = {}
        for char in s:
            if char in freq:
                freq[char] += 1
            else:
                freq[char] = 1
        
        # Now we simply subtract, if anything goes below 0 or does not exist, then false
        for char in t:
            val = freq.setdefault(char, 0)
            if val == 0:
                return False
            else:
                freq[char] -= 1
        
        # Need to check for remainders
        for key,val in freq.items():
            if val > 0:
                return False
        return True

        """

        # This is just cleaner

        if len(s) != len(t):
            return False
        
        freq = {}
        for i in range(len(s)):
            val_s = freq.setdefault(s[i], 0)
            val_t = freq.setdefault(t[i], 0)
            freq[s[i]] += 1
            freq[t[i]] -= 1
        for key, val in freq.items():
            if val != 0:
                return False

        return True