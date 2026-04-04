class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1

        while left < right:
            mid = (left+right) // 2
            print(f"mid is {mid}")
            if nums[mid] == target:
                return mid
            if target > nums[mid]:
                print(f"{nums[mid]} is smaller than")
                left = mid + 1
            else:
                right = mid - 1
        if nums[left] == target:
            return left
        return -1
            

