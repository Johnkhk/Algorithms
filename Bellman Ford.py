from collections import defaultdict
import heapq
### Djikstras ###
# path with max probability #
n=3
edges=[[0,1],[1,2],[0,2]]
succProb=[0.5,0.5,0.3]
start,end=0,2
## Build a graph ##
adj=defaultdict(list)
for i,(e,v) in enumerate(edges):
    adj[e].append([succProb[i],v])
    adj[v].append([succProb[i],e])

## cache for answer ##
# costs=[float("inf")]*n # mindist
costs=[0]*n # maxdist
costs[start]=1 # start has to be 1
h = [(1,start)]
while h:
    cost,node = heapq.heappop(h)
    cost=abs(cost)
    for edgecost,child in adj[node]:
        if costs[node] * edgecost > costs[child]: # only up date if bigger
            costs[child] = costs[node] * edgecost
            heapq.heappush(h,(-costs[child] * edgecost,child)) # negative to get max edge

print(costs[end])