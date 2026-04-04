class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        
        frontW, backW = len(matrix[0])-1,0
        frontL, backL = len(matrix)-1, 0
        middleW, middleL = 0,0

        # Finding the row first
        while frontL >= backL:
            middleL = (frontL + backL) // 2
            currVal = matrix[middleL][-1]
            if currVal < target:
                backL = middleL + 1
            elif currVal > target:
                frontL = middleL - 1
            elif currVal == target:
                return True
        
        row = backL
        if row >= len(matrix):
            return False

        while frontW >= backW:
            middleW = (frontW + backW) // 2
            currVal = matrix[row][middleW]
            if currVal < target:
                backW = middleW + 1
            elif currVal > target:
                frontW = middleW - 1
            elif currVal == target:
                return True
        
        return False