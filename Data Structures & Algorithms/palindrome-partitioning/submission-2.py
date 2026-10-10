class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        def isPalindrome(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True
        
        
        res = []

        def backtrack(i, j, cur):
            if i == len(s):
                if len(cur) > 0:
                    res.append(cur.copy())
                return
            
            if j > len(s):
                return
            
            # include Palindrome
            if isPalindrome(i,j-1) and s[i:j] != "":
                cur.append(s[i:j])
                newI = j
                newJ = j+1
                backtrack(newI, newJ, cur)
                cur.pop()

            # Not include Palindrome
            backtrack(i, j+1, cur)

        backtrack(0, 0, [])

        return res