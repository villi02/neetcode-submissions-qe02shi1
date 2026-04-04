class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i in range(len(nums)):
            num = nums[i]
            needed = target - num
            if needed in seen:
                return [seen[needed], i]
            else:
                seen[num] = i
        return [0,0]