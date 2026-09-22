class PrefixTree:

    def __init__(self):
        self.root = {}
        self.IsWord = {}

    def insert(self, word: str) -> None:
        wordList = list(word)
        def recInsert(wrd, curr):
            if not wrd:
                return
            
            nextChar = wrd.pop(0)

            if nextChar not in curr:
                curr[nextChar] = {}
            curr = curr[nextChar]

            recInsert(wrd, curr)
        node = self.root
        recInsert(wordList, node)

        self.IsWord[word] = True



    def search(self, word: str) -> bool:
        wordList = list(word)
        if word not in self.IsWord:
            return False
        return True

        

    def startsWith(self, prefix: str) -> bool:
        wordList = list(prefix)

        node = self.root
        while wordList:
            nextChar = wordList.pop(0)
            if nextChar not in node:
                return False
            else:
                node = node[nextChar]
        return True
        
        