class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1]*len(nums)
        
        for i in range(len(nums)):
            for j in range(len(nums)):
                if j != i:
                    res[i] *= nums[j]

        return res