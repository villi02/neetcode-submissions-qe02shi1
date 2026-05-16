class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # We basically want to check if we can extend and what the area of the extensions is

        # Using stack to keep track of which can be extended, and where they start
        # We only pop if an element is smaller than the previous etc, then pop until they are not higher

        stack = [] # (start index, height)
        maxArea = 0

        for i, h in enumerate(heights):
            start = i

            while stack and stack[-1][1] > h: # The current one is smaller
                index, height = stack.pop()
                maxArea = max(maxArea, height*(i-index))
                print(f"maxArea using {height} starting at {index}")
                start = index
            
            stack.append((start, h))
            print(f"index in array:{i}, start:{start}, height:{h}")

        for indx, height in stack:
            maxArea = max(maxArea, height*(len(heights)-indx))
        
        return maxArea