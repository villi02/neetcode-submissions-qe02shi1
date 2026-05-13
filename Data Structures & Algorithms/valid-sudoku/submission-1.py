class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)

        # I think we can simply try the brute force of checking each row, column and then box

        # My intuition is telling me to use hashmap, maybe one for each row and column?

        for row in range(n): # Checking rows
            dups = {}
            for val in board[row]:
                if val != ".":
                    if val in dups:
                        return False
                    else:
                        dups[val] = 1
        
        for col in range(n): # Checking columns
            column = [row[col] for row in board]
            dups = {}
            for val in column:
                if val != ".":
                    if val in dups:
                        return False
                    else:
                        dups[val] = 1
        
        # Checking boxes
        for i in range(1, n, 3):
            for j in range(1, n, 3):
                center = [i,j]
                dups = {}
                # iterate through each box
                for k in [i-1, i, i+1]:
                    for p in [j-1,j,j+1]:
                        if board[k][p] != ".":
                            val = board[k][p]
                            if val in dups:
                                return False
                            else:
                                dups[val] = 1
        
        return True