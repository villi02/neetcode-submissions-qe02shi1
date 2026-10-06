class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        left = "("
        right = ")"

        res = []

        def backtrack(closedN, cur, openP):
            if openP == closedN == n:
                res.append("".join(cur))
                return
            
            # Condition for invalid string
            # Cant place a right without openP > 0

            
            if openP < n:
                # Two cases, put down left or right
                # Put down left
                cur.append(left)
                backtrack(closedN, cur, openP+1)
                cur.pop()
                

            if closedN < openP:
                cur.append(right)
                backtrack(closedN+1, cur, openP)
                cur.pop()
        
        backtrack(0, [], 0)

        return res
