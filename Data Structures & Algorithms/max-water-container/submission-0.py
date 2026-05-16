class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0,len(heights)-1

        maxWater = 0

        # starting from the outside, and the smallest one moves

        while left < right:
            h = min(heights[left], heights[right])
            maxWater = max(h * (right-left), maxWater)

            if heights[right] < heights[left]:
                right -= 1
            else:
                left += 1
        
        return maxWater
