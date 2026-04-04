class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Want to check for each of the words if an anagram exists, then group them toghether
        
        # Maybe we can hash the frequency?
        anagrams = {}
        for wrd in strs:
            occurance = [0] * 26
            for char in wrd:
                occurance[ord(char) - 97] += 1
            key = tuple(occurance)
            if key not in anagrams.keys():
                anagrams[key] = [wrd]
            else:
                anagrams[key].append(wrd)
        return list(anagrams.values())