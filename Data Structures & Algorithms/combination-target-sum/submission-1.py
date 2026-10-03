class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        # Basically turn this into a DFS of a binary tree

        res = []

        def DFS(i, cur, tot):
            # Base case
            if tot == target:
                res.append(cur.copy())
                return
            if tot > target or i >= len(nums):
                return
            
            # Basically make one where we include X, and one where we dont

            # Include X
            cur.append(nums[i])
            DFS(i, cur, tot+nums[i])

            # Not include X
            cur.pop()
            DFS(i+1, cur, tot)
        
        DFS(0, [], 0)

        return res
            