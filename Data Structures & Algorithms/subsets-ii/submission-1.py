class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []

        nums.sort()

        visited = {}

        def DFS(i, cur):
            if i == len(nums):
                pathString = "".join(str(val) for val in cur)
                if pathString not in visited:
                    res.append(cur.copy())
                    visited[pathString] = True
                return
            

            
            # Include i
            cur.append(nums[i])
            DFS(i+1, cur.copy())
            cur.pop()

            # not include i
            DFS(i+1, cur.copy())
        
        DFS(0, [])

        return res