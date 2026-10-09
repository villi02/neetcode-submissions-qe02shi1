class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        # Lets use a simpler approach now, with recursion
        ROWS = len(board)
        COLS = len(board[0])
        start = word[0]

        def dfs(x, y, depth, path):
            if depth == len(word):
                return True
            
            if (0 <= x < ROWS and 0 <= y < COLS 
            and word[depth] == board[x][y]
            and (x,y) not in path
            ):
                path.add((x,y))
                return (
                    dfs(x+1, y, depth+1, path.copy())
                    or dfs(x-1, y, depth+1, path)
                    or dfs(x, y+1, depth+1, path)
                    or dfs(x, y-1, depth+1, path)
                )
            
            return False
        
        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == start:
                    if dfs(i, j, 0, set()):
                        return True
        
        return False