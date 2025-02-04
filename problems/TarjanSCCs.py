from collections import defaultdict
### only makes sense in directed graph ###

edges = [[1,0],[0,2],[3,1],[3,2],[0,3]]
n = 4

time = 0
stack=[]
stackset=set()
res=[]
disc = [-1]*n
low = [-1]*n
adj=defaultdict(list)
for e,v in edges:
    adj[e].append(v)
def dfs(node,parent):
    global time
    disc[node]=low[node]=time
    time+=1
    stackset.add(node)
    stack.append(node)
    for child in adj[node]:
        if disc[child]==-1:
            dfs(child,None)
            low[node]=min(low[node],low[child])
        elif child in stackset:# backedge
            low[node] = min(low[node],disc[child])
        # elif parent!=child: # backedge or crossedge
            # if child in stackset:
    
    if disc[node]==low[node]:
        tmp=[]
        while stack[-1]!=node:
            item=stack.pop()
            stackset.remove(item)
            tmp.append(item)
        item=stack.pop()
        tmp.append(item)
        stackset.remove(node)
        res.append(tmp)

for i in range(n)            :
    if disc[i]==-1:
        dfs(i,None)
print(res)
