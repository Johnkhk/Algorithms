from collections import defaultdict


def dfs(node):
    visited.add(node)
    dfsvisited.add(node)
    for child in adj[node]:
        if child in visited and child in dfsvisited:
            return True #cycle
        elif child not in visited:
            if dfs(child):
                return True
    dfsvisited.remove(node)
    return False








visited = set()
dfsvisited = set()
prereqs = [[1,0],[2,0],[3,1],[3,2],[0,1]]
# prereqs = [[1,0],[2,0],[3,1],[3,2]]

numVertexes = 4
adj={i:[] for i in range(numVertexes)}
for totake, prereq in prereqs:
    adj[prereq].append(totake)

for i in range(numVertexes):
    if dfs(i):
        print("TRUE") # There is a cycle
        
