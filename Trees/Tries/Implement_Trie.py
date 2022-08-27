### Very self explanatory ###
### Use a Trienode, which has end of word and hashmap of children
class TrieNode:
    # Initialize your data structure here.
    def __init__(self):
        self.endWord=False # need this to know what words we have inserted
        self.children={}

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        tmp = self.root
        for c in word:
            if c not in tmp.children:
                tmp.children[c]=TrieNode()
            tmp = tmp.children[c]
        tmp.endWord=True
            
    def search(self, word: str) -> bool:
        tmp = self.root
        for c in word:
            if c not in tmp.children:
                return False
            tmp=tmp.children[c]
        return tmp.endWord==True
        

    def startsWith(self, prefix: str) -> bool:
        tmp = self.root
        for c in prefix:
            if c not in tmp.children:
                return False
            tmp=tmp.children[c]
        return True