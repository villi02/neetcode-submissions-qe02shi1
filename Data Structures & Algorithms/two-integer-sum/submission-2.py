class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        needed = {}
        for num in nums:
            need = target - num

            if num in needed:
                return [needed[num], len(needed)]
            else:
                needed[need] = len(needed)
        return [0,0]