class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        left = "("
        right = ")"

        res = []

        def backtrack(i, cur, openP):
            if i == n*2:
                if openP == 0:
                    res.append(cur)
                return
            
            # Condition for invalid string
            # Cant place a right without openP > 0

            
            else:
                # Two cases, put down left or right

                # Put down left
                if openP < n:
                    leftcur = cur + left
                    backtrack(i+1, leftcur, openP+1)
                

            if openP > 0:
                rightcur = cur + right
                backtrack(i+1, rightcur, openP-1)
        
        backtrack(0, "", 0)

        return res
