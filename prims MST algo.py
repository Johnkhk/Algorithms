# Prim's algorithm #
# Time: O(N^2 * log(N))
# Space: O(N^2)
import heapq
from collections import defaultdict
points=[[0,0],[2,2],[3,10],[5,2],[7,0]]
N=len(points)
#https://leetcode.com/problems/min-cost-to-connect-all-points/solution/
### Actually dont even need adjacency list
adj=defaultdict(list)
for i in range(N):
    for j in range(i+1,N):
        cost = abs(points[i][0]-points[j][0]) + abs(points[i][1]-points[j][1])
        adj[i].append([cost,j])
        adj[j].append([cost,i])
h=[[0,0]]
visited=set()
res=0
# while h:
c=0
while len(visited)<N: # This is more optimized
# while h:
    c+=1
    cost, node = heapq.heappop(h)
    if node in visited:
        continue
    visited.add(node)
    res+=cost
    for childcost, child in adj[node]:
        if child not in visited:
            heapq.heappush(h,[childcost,child])
print(res,c)