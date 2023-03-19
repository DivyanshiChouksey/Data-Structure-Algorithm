# Design Add and Search Words Data Structure

class TrieNode:
    def __init__(self):
        self.dct = {}
        self.isLast = False
    
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self,word):
        node = self.root
        for ch in word:
            if ch not in node.dct:
                node.dct[ch] = TrieNode()
            node = node.dct[ch]
        node.isLast = True
    
    def search(self, word):
        def helper(j,node):
            if j == len(word) and node.isLast==True:
                return True
            elif j == len(word):
                return False
            if word[j] !=".":
                if word[j] in node.dct:
                    return helper(j+1,node.dct[word[j]])
                return False
            else:
                for k,v in node.dct.items():
                    if helper(j+1,node.dct[k]):
                        return True   
            return False
        
        return helper(0,self.root)



obj = WordDictionary()
print(obj.addWord("bad"))
print(obj.addWord("dad"))
print(obj.addWord("mad"))

print(obj.search("pad"))
print(obj.search("bad"))
print(obj.search(".ad"))
print(obj.search("b.."))


"""
Input
["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
[[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
Output
[null,null,null,null,false,true,true,true]
"""