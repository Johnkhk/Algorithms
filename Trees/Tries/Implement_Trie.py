# TODO:
"""
wordsearch 2 is very hard... the backtracking is not too bad but the optimization needs review.
"""
################## Quick and Dirty Implementation ##################
# insert them into trie
words=["hey"]
WORD_KEY = '$'
trie = {}
for word in words:
    node = trie
    for letter in word:
        # retrieve the next node; If not found, create a empty node.
        node = node.setdefault(letter, {})
    # mark the existence of a word in trie node
    node[WORD_KEY] = word

################## Use a Trienode, which has end of word and hashmap of children ##################
class TrieNode:
    # Initialize your data structure here.
    def __init__(self):
        self.endWord=False # need this to know what words we have inserted
        self.children={}

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        tmp = self.root
        for c in word:
            if c not in tmp.children:
                tmp.children[c]=TrieNode()
            tmp = tmp.children[c]
        tmp.endWord=True
            
    def search(self, word):
        tmp = self.root
        for c in word:
            if c not in tmp.children:
                return False
            tmp=tmp.children[c]
        return tmp.endWord==True
        

    def startsWith(self, prefix):
        tmp = self.root
        for c in prefix:
            if c not in tmp.children:
                return False
            tmp=tmp.children[c]
        return True

################## DELETE FROM TRIE ##################

class Trie_del:
    WORD_END = "$" # Python static variable
    def __init__(self):
        self.trie = {}
    def insert(self, word):
        cur = self.trie
        for char in word:
            if char not in cur:
                cur[char] = {}
            cur = cur[char]
        cur[Trie_del.WORD_END] = word ### dirty trick to put the delete $ as the word

    def delete(self, word):
        def _delete(word, cur_trie, i=0):
            if i == len(word):
                if Trie_del.WORD_END not in cur_trie:
                    raise ValueError("'%s' is not registered in the trie..." %word)
                cur_trie.pop(Trie_del.WORD_END)
                if len(cur_trie) > 0:
                    return False
                return True
            if word[i] not in cur_trie:
                raise ValueError("'%s' is not registered in the trie..." %word)
            cont = _delete(word, cur_trie[word[i]], i+1)
            if cont:
                cur_trie.pop(word[i])
                if Trie_del.WORD_END in cur_trie:
                    return False
                return True
            return False
        _delete(word, self.trie)

################## EVEN BETTER, set the last word [key] to be the full word ##################
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        WORD_KEY = '$'
        
        trie = {}
        for word in words:
            node = trie
            for letter in word:
                # retrieve the next node; If not found, create a empty node.
                node = node.setdefault(letter, {})
            # mark the existence of a word in trie node
            node[WORD_KEY] = word
        
        rowNum = len(board)
        colNum = len(board[0])
        
        matchedWords = []
        
        def backtracking(row, col, parent):    
            
            letter = board[row][col]
            currNode = parent[letter]
            
            # check if we find a match of word
            word_match = currNode.pop(WORD_KEY, False)
            if word_match:
                # also we removed the matched word to avoid duplicates,
                #   as well as avoiding using set() for results.
                matchedWords.append(word_match)
            
            # Before the EXPLORATION, mark the cell as visited 
            board[row][col] = '#'
            
            # Explore the neighbors in 4 directions, i.e. up, right, down, left
            for (rowOffset, colOffset) in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                newRow, newCol = row + rowOffset, col + colOffset     
                if newRow < 0 or newRow >= rowNum or newCol < 0 or newCol >= colNum:
                    continue
                if not board[newRow][newCol] in currNode:
                    continue
                backtracking(newRow, newCol, currNode)
        
            # End of EXPLORATION, we restore the cell
            board[row][col] = letter
        
            # Optimization: incrementally remove the matched leaf node in Trie.
            if not currNode:
                parent.pop(letter)

        for row in range(rowNum):
            for col in range(colNum):
                # starting from each of the cells
                if board[row][col] in trie:
                    backtracking(row, col, trie)
        
        return matchedWords 

if __name__=='__main__':
    pass
    # t = Trie_del()
    # t.insert("bar")
    # t.insert("baraka")
    # t.insert("barakalar")

    # t.delete("barak") # raises error as 'barak' is not a valid WORD_END although it is a valid path.
    # t.delete("bareka") # raises error as 'e' does not exist in the path.
    # t.delete("baraka") # deletes the WORD_END of 'baraka' without deleting any letter as there is 'barakalar' afterwards.
    # t.delete("barakalar") # deletes until the previous word (until the first Trie.WORD_END; "$" - by going backwards with recursion) in the same path (until 'baraka').