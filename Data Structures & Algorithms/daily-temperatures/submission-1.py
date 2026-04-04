class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        # Brute force
        """
        res = [0] * len(temperatures)
        for i, current in enumerate(temperatures):
            days_ahead = -1
            for j in range(i, len(temperatures)):
                print(f"i {i}, j {j}")
                if temperatures[j] > current:
                    res[i] = j - i
                    days_ahead = j-i
                    break
        return res
        """

        # O(n), O(n) solution
        res = [0] * len(temperatures)

        stack = [] # "[temp, index]"
        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                stackTemp, stackIdx = stack.pop()
                res[stackIdx] = i - stackIdx
            stack.append([temp, i])

        return res
        