class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        
        ROWS,COLS = len(board),len(board[0])
        visited = set()
        
        directions = [(-1,-1),(0,-1),(1,-1),(1,0),(1,1),(0,1),(-1,1),(-1,0)]

        def dfs(r,c):
            """
            Idea is to set first then go, that way the recursion knows to stop
            """
            if r<0 or c<0 or r>=ROWS or c>=COLS:
                return 
            if board[r][c]!="E":
                return
            
            mines=0
            for x,y in directions:
                if r+x>=0 and r+x<ROWS and c+y>=0 and c+y<COLS and board[r+x][c+y]=="M":
                    mines+=1
            if mines==0:
                board[r][c]="B"
            else:
                board[r][c]=str(mines)
                return
            
            for x,y in directions:
                dfs(r+x,c+y)
            
        
        # for r,c in click:
        r,c = click
        if board[r][c]=="M":
            board[r][c]="X"
            return board
        if board[r][c]=="E":
            dfs(r,c)
        return board
                

                