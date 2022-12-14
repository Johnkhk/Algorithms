
        
edges = [[1,2],[1,3],[2,3]]

### Union Find by rank ### with path compression
# redundant connection
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
    