class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        patternA = {}
        patternB = {}
        words = s.split(" ")

        if len(words) != len(pattern):
            return False

        for i in range(len(pattern)):
            if pattern[i] in patternA and patternA[pattern[i]] != words[i]:
                return False
            elif words[i] in patternB and patternB[words[i]] != pattern[i]:
                return False
            else:
                patternA[pattern[i]] = words[i]
                patternB[words[i]] = pattern[i]
            #print(patternA[pattern[i]] + words[i])
        
        return True
            