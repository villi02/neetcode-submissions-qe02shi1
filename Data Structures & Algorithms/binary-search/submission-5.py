class Solution:
    def search(self, nums: List[int], target: int) -> int:
        front, back = len(nums)-1, 0
        while front >= back:
            middleIndex = (front+back)//2
            if nums[middleIndex] > target:
                front = middleIndex - 1
            elif nums[middleIndex] < target:
                back = middleIndex + 1
            elif nums[middleIndex] == target:
                return middleIndex
        return -1