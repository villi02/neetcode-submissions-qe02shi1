class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        highest_at = [0] * len(arr)

        maxxx = float("-infinity")
        for i in range(len(arr)-1, -1, -1):
            maxxx = max(arr[i], maxxx)
            highest_at[i] = maxxx
        
        for i in range(len(arr)-1):
            arr[i] = highest_at[i+1]
        
        arr[-1] = -1

        return arr