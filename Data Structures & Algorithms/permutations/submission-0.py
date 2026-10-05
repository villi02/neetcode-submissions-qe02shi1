class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        res = []

        def DFS(i, cur, numsLeft):
            # Base case
            if len(cur) == len(nums):
                res.append(cur.copy())
                return
            
            # Else

            # For each value, we fix it at index this index, then continue
            tempNumsLeft = numsLeft.copy()
            for val in numsLeft:
                cur.append(val)
                tempNumsLeft.remove(val)
                DFS(i+1, cur.copy(), tempNumsLeft.copy())
                print(f"current: {cur}, and now adding val {val} and index {i}, we have numsLeft: {tempNumsLeft}")
                tempNumsLeft.append(val)
                cur.pop()
        
        DFS(0, [], nums)

        return res
