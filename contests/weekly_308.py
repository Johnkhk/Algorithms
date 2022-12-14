### 2392. Build a Matrix With Conditions ###
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
    