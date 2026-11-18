class TrieNode:

    def __init__(self):
        self.children = [None] * 26
        self.isEndOfWord = False
        

class PrefixTree:
    def __init__(self):
        self.root = TrieNode()


    def insert(self, word: str) -> None:
        cur = self.root

        for c in word:
            index = ord(c) - ord('a')
            if cur.children[index] == None:
                new_node = TrieNode()
                cur.children[index] = new_node
            cur = cur.children[index]
        cur.isEndOfWord = True


    def search(self, word: str) -> bool:
        cur = self.root
        for c in word:
            index = ord(c) - ord('a')
            if cur.children[index] is None:
                return False
            cur = cur.children[index]
        return cur.isEndOfWord

        

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        word = prefix
        for c in word:
            index = ord(c) - ord('a')
            if cur.children[index] == None:
                return False
            cur = cur.children[index]
        return True
        
        