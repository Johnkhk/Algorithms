from collections import defaultdict

### Method 1 Union Find ###
# Union Find only works for Undirected graph
# If edges not N-1, where N is vertexes, then will have multiple component

edges = [[1,2],[1,3],[2,3]]
par = [i for i in range(len(edges)+1)]
rank = [1]*(len(edges)+1)

def find(node):
    p = par[node]
    while p!= par[p]:
        par[p]=par[par[p]] #path compression
        p = par[p]
    return p
def union(node1,node2):
    p1,p2 = find(node1),find(node2)
    if p1==p2:
        return False # we found a cycle | redundant connection
    if rank[p1] < rank[p2]:
        par[p1]=p2
        rank[p2]+=rank[p1]
    else:
        par[p2]=p1
        rank[p1]+=rank[p2]
    return True # successful union
for n1,n2 in edges:
    if not union(n1,n2):
        print([n1,n2])
        # return [n1,n2]

### Method 2 DFS ###
# Logic is: if we DFS and we hit a node which is in visited, but not our own parent, then we have a cycle!


print("#"*30)
# edges = [[1,2],[1,3],[2,3]]#cycle
edges = [[1,2],[1,3],[2,4],[4,5],[5,1]]#nocycle
adj = defaultdict(list)
for a,b in edges:
    adj[a].append(b)
    adj[b].append(a)
visited = set()
def dfs(node,parent):
    visited.add(node)
    for child in adj[node]:
        if child not in visited:
            if dfs(child,node):
                return True
        elif parent !=child:
            return True
    return False
for a,b in adj.items():
    if a not in visited and dfs(a,None):
        print("CYCLE")