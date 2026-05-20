class Solution:
    def trap(self, height: List[int]) -> int:

        """
        # Want to keep track of how far we can extend the current bars etc

        stack = [] # (index, height)
        found = {}
        water = 0
        start = 0
        for i, bar in enumerate(height):
            while stack and bar >= stack[-1][1]: # Cannot be extended any futher
                index, h = stack.pop()
                water += min(h, bar) * (i - index-1) - sum(height[index+1:i]) # removing the height between
                start = index
            stack.append((i, bar))
        return water
        """
        if not height:
            return 0
        # Using two pointers
        l , r = 0, len(height)-1
        maxl, maxr = height[l], height[r]
        water = 0

        while l<r:
            if maxl < maxr:
                l += 1
                maxl = max(maxl, height[l])
                water +=  maxl - height[l]
            else:
                r -= 1
                maxr = max(maxr, height[r])
                water += maxr-height[r]
        return water
