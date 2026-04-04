class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        front, back = len(numbers) - 1, 0
        while front > back:
            tot = numbers[front] + numbers[back]
            if (tot - target) > 0: # Too big
                front -= 1
            elif (tot - target) < 0: # Too small
                back += 1
            else:
                return [back+1, front+1]