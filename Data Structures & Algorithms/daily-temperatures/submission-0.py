class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Brute force
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

        