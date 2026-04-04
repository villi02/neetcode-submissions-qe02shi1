class Solution:
    def search(self, nums: List[int], target: int) -> int:
        front, back = len(nums)-1, 0
        while front >= back:
            middleIndex = (front+back)//2
            if nums[middleIndex] > target:
                front -= 1
            if nums[middleIndex] < target:
                back += 1
            if nums[middleIndex] == target:
                return middleIndex
        return -1