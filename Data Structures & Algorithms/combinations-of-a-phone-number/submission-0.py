class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []

        mapping = {"2": ["a", "b", "c"], "3": ["d", "e", "f"],
                    "4": ["g", "h", "i"], "5": ["j", "k", "l"],
                    "6": ["m", "n", "o"], "7": ["p", "q", "r", "s"],
                    "8": ["t", "u", "v"], "9": ["w", "x", "y", "z"]}
        

        def backtrack(i, cur):
            if i == len(digits):
                if cur != "":
                    res.append(cur)
                return
            
            
            for cand in mapping[digits[i]]:
                backtrack(i+1,cur+cand)
            return
        
        backtrack(0, "")

        return res