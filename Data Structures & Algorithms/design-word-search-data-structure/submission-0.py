class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.isEndOfWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root

        for c in word:
            index = ord(c) - ord('a')
            if cur.children[index] == None:
                new_node = TrieNode()
                cur.children[index] = new_node
            cur = cur.children[index]
        cur.isEndOfWord = True
        

    def search(self, word: str) -> bool:
        def dfs(j, node):

            cur = node

            for i in range(j, len(word)):

                c = word[i]

                # wildcard
                if c == ".":

                    for child in cur.children:

                        if child and dfs(i + 1, child):
                            return True

                    return False
                else:
                    index = ord(c) -ord('a')
                    if cur.children[index] is None:
                        return False            
                    cur = cur.children[index]
            return cur.isEndOfWord
        
        return dfs(0, self.root)
        
