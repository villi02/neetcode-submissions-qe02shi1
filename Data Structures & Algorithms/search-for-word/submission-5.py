class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        visited = [[False for _ in range(len(board[0]))] for _ in range(len(board))]

        start = word[0]

        def get_neighbors(x, y, target):
            gridpoints = [[x+1, y], [x-1,y], [x, y+1], [x, y-1]]
            neigh = []

            for newX, newY in gridpoints:
                if -1 < newX < len(board) and -1 < newY < len(board[0]):
                    if board[newX][newY] == target and not visited[newX][newY]:
                        neigh.append([newX, newY])
            return neigh

        def find_Word(x, y, word, depth, path):
            if depth == len(word):
                return True
            

            neighbors = get_neighbors(x,y, word[depth])
            for nX, nY in neighbors:
                strpath = (nX,nY)
                if strpath not in path:
                    newPath = path.copy()
                    newPath[strpath] = True
                    if find_Word(nX, nY, word, depth+1, newPath):
                        return True
            return False


        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == start: # Here we need to expand
                    startPath = (i,j)
                    if find_Word(i,j, word, 1, {startPath:True}):
                        return True
        
        return False