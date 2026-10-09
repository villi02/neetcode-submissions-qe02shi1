class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        res = []

        def is_palindrome(seq):
            return seq[::-1] == seq # not optimal, better to do with two pointers

        def backtrack(i, j, cur):
            # Base case
            if i == len(s):
                if len(cur) > 0:
                    res.append(cur.copy())
                return
            if j > len(s):
                return

            if is_palindrome(s[i:j]) and s[i:j] != "": # Partition here
                cur.append(s[i:j])
                newI = j
                newJ = j+1
                backtrack(newI, j+1, cur)
                cur.pop()
            
            # Not partition here
            backtrack(i, j+1,cur)

        backtrack(0,0,[])

        return res
            