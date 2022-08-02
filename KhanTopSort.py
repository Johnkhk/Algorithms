
# Time: O(V+E)
# Space: O(V)

from collections import deque
numCourses = 4
prerequisites = [[1,0],[2,0],[3,1],[3,2],[0,1]]

q = []
adj = {i:[] for i in range(numCourses)}
indegree = {i:0 for i in range(numCourses)}
# in the D-Graph prereq->course
for totake, prereq in prerequisites:
    adj[prereq].append(totake)
    indegree[totake]+=1
    
# Add indegree 0 keys into queue
q = deque([key for key,val in indegree.items() if val==0])
ans=[]
while q:
    node = q.pop()
    ans.append(node)
    for child in adj[node]:
        indegree[child]-=1
        if indegree[child]==0:
            q.append(child)
if len(ans)!=numCourses:
    print([])
    # return []
print(ans)
# return ans