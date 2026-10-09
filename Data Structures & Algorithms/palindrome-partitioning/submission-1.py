class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        res = []

        def is_palindrome(l,r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True            

        def backtrack(i, j, cur):
            # Base case
            if i == len(s):
                if len(cur) > 0:
                    res.append(cur.copy())
                return
            
            if j > len(s):
                return

            if is_palindrome(i, j-1) and s[i:j] != "": # Partition here
                cur.append(s[i:j])
                newI = j
                newJ = j+1
                backtrack(newI, j+1, cur)
                cur.pop()
            
            # Not partition here
            backtrack(i, j+1,cur)

        backtrack(0,0,[])

        return res
            