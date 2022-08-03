        
n=5
edges=[[0,1],[1,2],[0,2],[3,4]]
par = [i for i in range(n)]
rank = [1]*n

adj = {i:[] for i in range(n)}
        
for k, v in edges:
    adj[k].append(v)
    adj[v].append(k)

def dfs(node):
    # if not node:
    #     return
    visited.add(node)
    for n in adj[node]:
        if n not in visited:
            dfs(n)
# print(adj)
cc=0
visited = set()
for i in range(n):
    if i in visited:
        continue
    dfs(i)
    cc+=1
    # print("hi", visited)
    
print(cc)
    