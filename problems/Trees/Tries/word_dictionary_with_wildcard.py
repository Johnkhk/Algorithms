### Hashmap of level:to set of words solution ###
# TC: O(MN) for search, where M=length of word and N is # of words. (degrades to N^2M) for large datasets
# SC: Huge 
class WordDictionary:
    def __init__(self):
        self.d = defaultdict(set)


    def addWord(self, word: str) -> None:
        self.d[len(word)].add(word)


    def search(self, word: str) -> bool:
        m = len(word)
        for dict_word in self.d[m]:
            i = 0
            while i < m and (dict_word[i] == word[i] or word[i] == '.'):
                i += 1
            if i == m:
                return True
        return False

### Trie Solution ###
# Searching is O(M) for good words, and O(26^M) for bad words
class TrieNode:
    def __init__(self):
        self.endWord=False # need this to know what words we have inserted
        self.children={}
        
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        # dot = self.root
        tmp = self.root
        for c in word:
            if c not in tmp.children:
                newTrieNode=TrieNode()
                tmp.children[c]=newTrieNode
                # dot.children['.']=newTrieNode
            tmp=tmp.children[c]
            # dot=dot.children['.']
        tmp.endWord=True
        # dot.endWord=True
        
        

    def search(self, word: str) -> bool:
        
        def dfs(idx,root):
            """
            dfs needed for ".", check for all children starting at index j of word that we match
            """
            tmp = root
            i=0
            for i in range(idx,len(word)):
                c=word[i]
                if c=='.':
                    for child in tmp.children.values():
                        if dfs(i+1,child):
                            return True
                if c not in tmp.children:
                    return False
                tmp=tmp.children[c]
                i+=1
            return tmp.endWord==True
        return dfs(0,self.root)
