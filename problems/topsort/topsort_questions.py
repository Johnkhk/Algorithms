class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        #Q4: create 2 graphs (1 for rowConditions and 1 for colConditions) and do topological sorting. This sort gives us the row and col index in which particular number appears. If any of two graphs are cyclic, then return empty list other wise new list created by topo-sort indexes.
        
        def khantopsort(edges):
            adj = {i:[] for i in range(1,k+1)}
            indegree={i:0 for i in range(1,k+1)}
            for e,v in edges:
                adj[e].append(v)
                indegree[v]+=1
            q=deque()
            for key in indegree:
                if indegree[key]==0:
                    q.append(key)
            ans=[]
            count=0
            while q:
                node = q.popleft()
                count+=1
                ans.append(node)
                for child in adj[node]:
                    indegree[child]-=1
                    if indegree[child]==0:
                        q.append(child)
            if count!=k:
                return None
            
            return ans
        a = khantopsort(rowConditions)
        b = khantopsort(colConditions)
        if not a or not b:
            return []
        rx = {i:j for j,i in enumerate(a)}
        cx = {i:j for j,i in enumerate(b)}        
        ans = [[0]*k for i in range(k)]
        # print(rx,cx)
        for i in range(1,k+1):
            ans[rx[i]][cx[i]]=i
        return ans
            
            
        
        
        
        
        
        
        


class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        #Q4: create 2 graphs (1 for rowConditions and 1 for colConditions) and do topological sorting. This sort gives us the row and col index in which particular number appears. If any of two graphs are cyclic, then return empty list other wise new list created by topo-sort indexes.
        
        def dfstopsort(edges):
            adj = {i:[] for i in range(1,k+1)}
            for e,v in edges:
                adj[e].append(v)
            seen=set()
            dfsvisited=set()
            ans=[]
            flag=False
            def dfs(i):
                nonlocal flag
                seen.add(i)
                dfsvisited.add(i)

                for child in adj[i]:
                    if child in seen and child in dfsvisited:
                        flag=True
                        return False
                    if child not in seen:
                        dfs(child)
                dfsvisited.remove(i)
                ans.append(i)
                return True
            for i in range(1,k+1):
                if i not in seen:
                    dfs(i)
                    if flag:
                        return None
            
            return ans[::-1]
        a = dfstopsort(rowConditions)
        b = dfstopsort(colConditions)
        if not a or not b:
            return []
        rx = {i:j for j,i in enumerate(a)}
        cx = {i:j for j,i in enumerate(b)}        
        ans = [[0]*k for i in range(k)]
        print(rx,cx)
        for i in range(1,k+1):
            ans[rx[i]][cx[i]]=i
        return ans
            
            
        
        
        
        
        
        
        