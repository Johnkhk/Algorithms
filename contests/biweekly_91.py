### q2
# very good solutions
# https://leetcode.com/problems/count-ways-to-build-good-strings/solutions/2807396/python-c-iterative-recursive-dp-solutions-explained/


### q3 
### lee215 solution, i dont get it
class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        n = len(edges) + 1
        adj = [[] for i in range(n)]
        for i,j in edges:
            adj[i].append(j)
            adj[j].append(i)
        seen = set()

        def dfs(i, d0):
            seen.add(i)
            res = -inf
            db = 0 if i == bob else n
            
            for j in adj[i]:
                if j in seen: continue
                    
                cur, kk = dfs(j, d0 + 1)
                res = max(res, cur)
                db = min(db, kk)
                
            if res == -inf: res = 0
            if d0 == db: res += amount[i] // 2
            if d0 < db: res += amount[i]
            return res, db + 1

        return dfs(0, 0)[0]

