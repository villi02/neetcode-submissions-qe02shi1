class Solution:
    def findMin(self, nums: List[int]) -> int:
        # I feel like nothing about the binary search changes except for the update logic here

        l, h = 0, len(nums)-1

        if nums[l] < nums[h]:
            return nums[l]

        while abs(l-h) > 1:
            # Change l and h if makes sense, else continue with normal b-search
            # Not sure about this approach anymore

            mid = (l+h)//2

            if nums[mid] < nums[h]:
                h = mid
            else:
                l = mid
        return nums[h]