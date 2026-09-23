class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        res = deque()
        res.append(-1)

        maxx = arr[-1]
        for i in range(len(arr)-1,0, -1):
            maxx = max(maxx, arr[i])
            res.appendleft(maxx)
        
        return list(res)
