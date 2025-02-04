class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()
        for word in words:
            trie.insert(word)
        
        ROWS,COLS = len(board),len(board[0])
        dirs = [(0,1),(0,-1),(1,0),(-1,0)]
        res=[]
        
        def dfs(i,j,curWord,curNode):
            if curNode.end==True:
                res.append(curWord)
                curNode.end=False
                
            if i<0 or j<0 or i>=ROWS or j>=COLS:
                return False
            
            tmp = board[i][j]
            if tmp not in curNode.children:
                return False
            curNode = curNode.children[tmp]
         
            
            board[i][j]='#'
            
            for x,y in dirs:
                dfs(x+i,y+j,curWord+tmp,curNode)
                    
            board[i][j]=tmp
        
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                dfs(i,j,"",trie.root)
        return res