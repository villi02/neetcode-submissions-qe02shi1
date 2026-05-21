class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        print(f"l {l}, r {r}")
        max_iter = 15
        iterr = 0
        while l <= r:
            iterr += 1
            if iterr > max_iter:
                return -1
            mid = (l+r) // 2
            if nums[mid] == target:
                return mid
            
            if nums[l] <= nums[mid]: # Left is sorted
                if nums[l] <= target < nums[mid]:
                    r = mid -1
                else:
                    l = mid +1
            else: # Right is sorted
                if nums[mid] < target <= nums[r]:
                    l = mid+1
                else:
                    r = mid-1
        return -1