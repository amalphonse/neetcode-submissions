class TrieNode:
    def __init__(self):
        self.children={}
        self.is_end=False

class PrefixTree:

    def __init__(self):
        self.root=TrieNode()

    def insert(self, word: str) -> None:
        node=self.root
        for w in word:
            if w not in node.children:
                node.children[w]=TrieNode()
            node=node.children[w]
        node.is_end=True

    def search(self, word: str) -> bool:
        node=self._find(word)
        return node is not None and node.is_end
        

    def startsWith(self, prefix: str) -> bool:
        return self._find(prefix) is not None
    

    def _find(self,s: str):
        node=self.root
        for ch in s:
            if ch not in node.children:
                return None
            node=node.children[ch]
        return node        
        