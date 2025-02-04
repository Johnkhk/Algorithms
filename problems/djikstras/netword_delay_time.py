### 743. Network Delay Time ###
"""
goal: find minum time it takes for all nodes to recieve signal
idea:
    build an adjancency map of lists
    key:source, value: list of (target,time) it takes
    then we BFS the map with a queue starting at node k, 
    
    e.g: q: [(2,0)]
    holding the finaltime counter, and the node we decrement the map 
    accordingly and add its children to the q when its time to finish zero
    
    Did not get. Had to look at solution 
    But solution is pretty easy:
    build a adj list: same as my intuition
    use a minheap and actually add to it (receivedat + childtime, child)
    edgecase: return res instead of finaltime in case visited is activated.
"""

### Djikstra's ###
### True Djikstra's uses V nodes in heap ###
"""
V is total nodes, E is total edges
TC: 
    O(E) to build adj list
    Worst case, every edge is in priority queue
    Popping takes O(Elog(E)), because we add edges to the queue
    however since max(E) = V*(V-1) ~ V^2, then O(logE) = O(logN^2) = O(2logN) = O(logN)
    therefore it is cool to say O(E+Vlog(E))
    So total TC: O(E+Vlog(V))
SC:
    # adj in worst case holds O(E*V)
    adj holds O(E) edges
    heap hold O(E) edges worst case
    and visited in worst case holds O(V) nodes
    so in total O(V+E)

"""
adj = defaultdict(list)

for source,target,time in times:
    adj[source].append((target,time))

h=[(0,k)]
# q=[(k,0)]
count=0
visited=set()
while h:
    finaltime,node = heapq.heappop(h)
    if node in visited:
        continue
    visited.add(node)
    count+=1
    res=finaltime
    if node in adj:    
        for i in range(len(adj[node])):
            child,time = adj[node][i]
            
            # adj[node][i] = (child,time-1)
            # q.append((finaltime+1,child))
            heapq.heappush(h,(finaltime+time,child))
if count!=n:
    return -1
return res

### DFS ###
"""
DFS:
    idea is to assign each signal a recievedat value
    initially set all to infinity
    use dfs and only update the nodes only if they are smaller
    TC: O((N-1)! + ElogE)
    SC: O(E) for recursion, O(N) for signalReceivedAt, O(E) for adj
"""
adj = defaultdict(list)

for source,target,time in times:
    adj[source].append((target,time))
for _ in adj.keys():
    adj[_].sort(key = lambda x:x[1])
signalReceivedAt = [float("inf") for i in range(n)]

def dfs(node,curtime):
    if curtime>=signalReceivedAt[node-1]:
        return
    signalReceivedAt[node-1] = curtime
    if node in adj:
        for child,time in adj[node]:
            dfs(child,time+curtime)
dfs(k,0)
res=max(signalReceivedAt)
if res == float("inf"):
    return -1
return res

### BFS (Shortes Path First Algorithm) ###
