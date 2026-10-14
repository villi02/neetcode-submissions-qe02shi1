class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        #cols = [False for _ in range(n)]
        rows = [False for _ in range(n)]
        diag1 = set()
        diag2 = set()

        def backtrack(c, cur, rows):
            if c == n:
                res.append(["".join(row) for row in cur])
                return 
            
            # Iterate through the columns

            # Include current row
            candidates = [i for i in range(n) if not rows[i] and c-i not in diag1 and c+i not in diag2]

            if len(candidates) <1: # No more places to put queen
                return
            for cand in candidates:
                cur[cand][c] = "Q"
                rows[cand] = True
                diag1.add(c-cand)
                diag2.add(c+cand)
                backtrack(c+1, cur, rows)

                diag1.remove(c-cand)
                diag2.remove(c+cand)
                
                cur[cand][c] = "."
                rows[cand] = False
        
        start = [[ "." for _ in range(n)] for _ in range(n)]
        backtrack(0, start, rows)

        return res