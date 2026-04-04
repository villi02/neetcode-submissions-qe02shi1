class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        needed_num = {}

        for i in range(len(nums)):
            needed = target - nums[i]
            if needed in needed_num.keys():
                return [needed_num[needed], i]
            else:
                needed_num[nums[i]] = i
        return []