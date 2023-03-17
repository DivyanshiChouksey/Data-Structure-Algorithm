# Implement Trie (Prefix Tree)


class TrieNode:
    def __init__(self):
        self.dct = {}
        self.isLast = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self,word):
        node = self.root
        for ch in word:
            if ch not in node.dct:
                node.dct[ch] = TrieNode()
            node = node.dct[ch]  
        node.isLast = True

    def search(self,word):
        node = self.root
        for ch in word:
            if ch not in node.dct:
                return False
            node = node.dct[ch]  
        return node.isLast

    def startsWith(self, prefix):
        node = self.root
        for ch in prefix:
            if ch not in node.dct:
                return False
            node = node.dct[ch]  
        return True
    


obj = Trie()
print(obj.insert("apple"))
print(obj.search("apple"))
print(obj.search("app"))
print(obj.startsWith("app"))
print(obj.insert("app"))
print(obj.search("app"))

