class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def Backtrack(i, cur):
            # Base case
            if i == len(nums):
                res.append(cur[::])
                return
            

            # Include nums[i]
            cur.append(nums[i])
            Backtrack(i+1, cur)
            cur.pop()

            # skip to avoid duplicates
            while i +1 < len(nums) and nums[i] == nums[i+1]:
                i+=1

            # Not include nums[i]
            Backtrack(i+1, cur)

        Backtrack(0, [])

        return res