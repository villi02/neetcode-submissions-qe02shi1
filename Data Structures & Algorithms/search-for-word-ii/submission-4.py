class TrieNode():
    def __init__(self):
        self.endOfWord = False
        self.children = {}
    
class Trie():
    def __init__(self):
        self.root = TrieNode()
    
    def add(self, word):
        curr = self.root

        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.endOfWord = True


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        def get_neighbors(board, i, j):
            adj = [(0,1), (1,0), (-1,0), (0,-1)]
            res = []
            for x, y in adj:
                newX = x+i
                newY = y+j

                if 0 <= newX < len(board):
                    if 0 <= newY < len(board[0]):
                        res.append((newX, newY))
            return res

                        
        
        # Populate Trie
        root = Trie()

        found = set()

        for word in words:
            root.add(word)

        visited = [[False for _ in range(len(board[0]))] for _ in range(len(board))]


        def DFS(i, j, node, path):
            if visited[i][j]:
                return
            
            if board[i][j] not in node.children:
                return
            
            visited[i][j] = True

            node = node.children[board[i][j]]
            newPath = path + board[i][j]
            if node.endOfWord:
                found.add(newPath)

            neighbors = get_neighbors(board, i,j)
            for x , y in neighbors:
                DFS(x,y, node, newPath)
            
            visited[i][j] = False

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] in root.root.children: # Do DFS from here
                    DFS(i,j, root.root, "")
                        
        
        return list(found)              