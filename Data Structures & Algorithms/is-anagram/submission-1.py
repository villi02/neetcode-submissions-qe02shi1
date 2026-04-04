class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Can do simply make a hashmap, where the value of each char is incremented when appears, then go through the other word and if any do not exist, go below 0 or are above 0 after, then not an anagram
        freq1 = {}
        freq2 = {}

        for char in s:
            if char not in freq1.keys():
                freq1[char] = 1
            else:
                freq1[char] += 1

        for char in t:
            if char not in freq2.keys():
                freq2[char] = 1
            else:
                freq2[char] += 1
        
        if len(freq1.keys()) != len(freq2.keys()):
            return False
        
        for key in freq1.keys():
            if key not in freq2.keys():
                return False
            else:
                if freq1[key] != freq2[key]:
                    return False
        return True

        # Now to find the O(n + m), and O(1) space.
        # What to do with the space O(1)
