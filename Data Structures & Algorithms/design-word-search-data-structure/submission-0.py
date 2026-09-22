class TreeNode:
    def __init__(self):
        self.children = {}


class WordDictionary:

    def __init__(self):
        self.root = {}

    def addWord(self, word: str) -> None:
        node = self.root
        for char in word:
            node = node.setdefault(char, {})
        node["#"] = True
        
        

    def search(self, word: str) -> bool:
        node = self.root
        def dfs(j, root):
            cur = root

            for i in range(j, len(word)):
                c = word[i]
                if c == ".":
                    for char, child in cur.items():
                        if char != "#" and dfs(i+1, child):
                            return True
                    return False
                else:
                    if c not in cur:
                        return False
                    cur = cur[c]
            return "#" in cur
        
        return dfs(0, self.root)