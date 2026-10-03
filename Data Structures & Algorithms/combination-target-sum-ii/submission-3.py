class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # Basically use the DFS framework to turn this into a binary tree

        res = []
        candidates.sort()

        def DFS(i, cur, tot):
            # Base case
            if tot == target:
                res.append(cur.copy())
                return
            if tot > target or i == len(candidates):
                return
            
            # Include X
            cur.append(candidates[i])
            DFS(i+1, cur, tot+candidates[i])
            cur.pop()

            # Not include X
            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            DFS(i+1, cur, tot)
        
        DFS(0, [], 0)

        return res