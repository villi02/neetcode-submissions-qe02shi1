class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dup = {}
        for num in nums:
            if num in dup.keys():
                return True
            else:
                dup[num] = 1
        return False