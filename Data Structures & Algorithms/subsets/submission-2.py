class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        # Basically reduce the problem to a dfs problem with two choices, include X or not include X

        res = []

        def DFS(i, cur):

            # base case
            if i >= len(nums): # hit the end of the line
                res.append(cur.copy())
                return
            
            # Including X
            cur.append(nums[i])
            DFS(i+1, cur)

            # Not including X
            cur.pop()
            DFS(i+1, cur)
        
        DFS(0, [])

        return res