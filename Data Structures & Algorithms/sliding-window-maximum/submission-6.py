class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # Keep track of a continously sorted array?
        # Use binary search for inserting and deleting?

        """
        def find_index(target, lst):
            l, r = 0, len(lst)
            while l < r:
                mid = (l+r) // 2
                if lst[mid] < target:
                    l = mid + 1
                else:
                    r = mid
            return l

        tracker = []
        res = []

        for i in range(k):
            tracker.append(nums[i])
        
        tracker.sort()

        l,r = 0, k
        res.append(tracker[-1])

        while r < len(nums):
            l += 1
            r += 1

            oldIndx = find_index(nums[l-1], tracker)
            tracker.pop(oldIndx)

            newIndx = find_index(nums[r-1], tracker)
            tracker.insert(newIndx, nums[r-1])


            res.append(tracker[-1])


        return res

        """

        # Using deque

        res = []
        q = deque()

        l = r = 0
        while r < len(nums):
            while q and nums[q[-1]] < nums[r]: # Popping smaller elements from q
                q.pop()
            q.append(r)

            if l > q[0]:
                q.popleft()
            
            if (r+1) >= k:
                res.append(nums[q[0]])
                l += 1
            r += 1
            
        return res


