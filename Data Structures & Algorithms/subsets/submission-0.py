class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        def helper(i, nums, curset, subsets):
            if i >= len(nums):
                subsets.append(curset.copy())
                return

            # Keep nums[i]
            curset.append(nums[i])
            helper(i+1, nums, curset, subsets)

            # Dont Keep nums[i]
            curset.pop()
            helper(i+1, nums, curset, subsets)

            return subsets

        curset, subset = [], []
        return helper(0, nums, curset, subset)